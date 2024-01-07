from flask import Flask, render_template, jsonify, request, redirect, url_for
from pymongo import MongoClient
from elasticsearch import Elasticsearch
from faker import Faker

# Initialize Flask app
app = Flask(__name__)
fake = Faker()

# MongoDB connection
mongo_client = MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client["ecommerce_db"]

# Elasticsearch connection
es_client = Elasticsearch("http://localhost:9200")

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/users')
def users():
    return render_template('users.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/sales')
def sales():
    return render_template('sales.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/kibana-dashboard')
def kibana_dashboard():
    return render_template('dashboard.html')

@app.route('/manage-item')
def manage_item():
    return render_template('manage-item.html')

@app.route('/api/sales', methods=['GET'])
def get_sales_data():
    sales_data = list(mongo_db.sales.find({}, {'_id': 0}))
    return jsonify(sales_data)

@app.route('/api/users', methods=['GET'])
def get_users_data():
    users_data = list(mongo_db.users.find({}, {'_id': 0}))
    return jsonify(users_data)

@app.route('/api/feedback', methods=['GET'])
def get_feedback_data():
    feedback_data = list(mongo_db.feedback.find({}, {'_id': 0}))
    return jsonify(feedback_data)

@app.route('/api/products', methods=['GET'])
def get_products_data():
    products_data = list(mongo_db.products.find({}, {'_id': 0}))
    return jsonify(products_data)

@app.route('/api/search', methods=['GET'])
def universal_search():
    query = request.args.get('query', '')
    response = es_client.search(
        index=["es_users_index", "es_products_index", "es_sales_index", "es_feedback_index"],
        body={
            "query": {
                "multi_match": {
                    "query": query,
                    "fields": ["name", "description", "email", "comment", "product_id", "user_id", "address", "category", "quantity", "rating"]
                }
            },
            "size": 50
        }
    )
    return jsonify([hit["_source"] for hit in response['hits']['hits']])

@app.route('/add-users', methods=['POST'])
def add_users():
    user_data = {
        'user_id': fake.uuid4(),
        'name': request.form.get('user_name'),
        'email': request.form.get('email'),
        'address': request.form.get('address'),
        'join_date': request.form.get('join_date'),
        'location': {
            "type": "Point",
            "coordinates": [
                0.0000,
                0.0000
            ]
        }
    }
    result = mongo_db['users'].insert_one(user_data)
    mongo_id = str(user_data.pop("_id", None))
    es_client.index(index='es_users_index', id=str(mongo_id), body=user_data)
    return redirect(url_for('index'))

@app.route('/add-products', methods=['POST'])
def add_products():
    product_data = {
        'product_id': fake.uuid4(),
        'name': str(request.form.get('product_name')),
        'description': str(request.form.get('description')),
        'price': float(request.form.get('price')),
        'category': str(request.form.get('category'))
    }
    result = mongo_db['products'].insert_one(product_data)
    mongo_id = str(product_data.pop("_id", None))
    es_client.index(index='es_products_index', id=mongo_id, body=product_data)
    return redirect(url_for('index'))

@app.route('/add-sales', methods=['POST'])
def add_sales():
    sale_data = {
        'sale_id': fake.uuid4(),
        'user_id': request.form.get('sale_user_id'),
        'product_id': request.form.get('sale_product_id'),
        'quantity': int(request.form.get('quantity')),
        'sale_date': request.form.get('sale_date')
    }
    result = mongo_db['sales'].insert_one(sale_data)
    mongo_id = str(sale_data.pop("_id", None))
    es_client.index(index='es_sales_index', id=str(mongo_id), body=sale_data)
    return redirect(url_for('index'))

@app.route('/add-feedback', methods=['POST'])
def add_feedback():
    feedback_data = {
        'feedback_id': fake.uuid4(),
        'user_id': request.form.get('feedback_user_id'),
        'product_id': request.form.get('feedback_product_id'),
        'rating': int(request.form.get('rating')),
        'comment': request.form.get('comment'),
        'feedback_date': request.form.get('feedback_date')
    }
    result = mongo_db['feedback'].insert_one(feedback_data)
    mongo_id = str(feedback_data.pop("_id", None))
    es_client.index(index='es_feedback_index', id=str(mongo_id), body=feedback_data)
    return redirect(url_for('index'))



if __name__ == "__main__":
    app.run(debug=True)
