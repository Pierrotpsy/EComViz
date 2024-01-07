from pymongo import MongoClient
from elasticsearch import Elasticsearch
import json

# Function to read data from a JSON file
def read_data_from_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Read data from the JSON files
user_data = read_data_from_file('data/user_data.json')
product_data = read_data_from_file('data/product_data.json')
sales_data = read_data_from_file('data/sales_data.json')
feedback_data = read_data_from_file('data/feedback_data.json')


# MongoDB Client Setup
mongo_client = MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client["ecommerce_db"] 

collections = ["users", "products", "sales", "feedback"]
for collection in collections:
    mongo_db[collection].drop()

users_collection = mongo_db["users"]
products_collection = mongo_db["products"]
sales_collection = mongo_db["sales"]
feedback_collection = mongo_db["feedback"]

# Function to insert data into MongoDB collection
def insert_data_to_mongodb(collection, data):
    collection.insert_many(data)

# Insert data into respective MongoDB collections
insert_data_to_mongodb(users_collection, user_data)
insert_data_to_mongodb(products_collection, product_data)
insert_data_to_mongodb(sales_collection, sales_data)
insert_data_to_mongodb(feedback_collection, feedback_data)

# Elasticsearch Client Setup
es_client = Elasticsearch("http://localhost:9200")

indices = ["es_users_index", "es_products_index", "es_sales_index", "es_feedback_index"]

if es_client.indices.exists(index="es_users_index"):
    es_client.indices.delete(index="es_users_index")

if es_client.indices.exists(index="es_products_index"):
    es_client.indices.delete(index="es_products_index")

if es_client.indices.exists(index="es_sales_index"):
    es_client.indices.delete(index="es_sales_index")

if es_client.indices.exists(index="es_feedback_index"):
    es_client.indices.delete(index="es_feedback_index")

def ingest_data_to_elasticsearch(mongo_collection, es_index, explicit_mapping=None):
    if explicit_mapping:
        es_client.indices.create(index=es_index, body=explicit_mapping)

    for document in mongo_collection.find():
        # Remove '_id' field
        mongo_id = str(document.pop("_id", None))
        es_client.index(index=es_index, id=mongo_id, body=document)

# Ingest data for each collection into corresponding Elasticsearch indices
users_mapping = {
    "mappings": {
        "properties": {
            "name": {"type": "text"},
            "email": {"type": "keyword"},
            "address": {"type": "text"},
            "join_date": {"type": "date", "format": "yyyy-MM-dd"},
            "location": {"type": "geo_shape"},
        }
    }
}
ingest_data_to_elasticsearch(users_collection, "es_users_index", users_mapping)
ingest_data_to_elasticsearch(products_collection, "es_products_index")
ingest_data_to_elasticsearch(sales_collection, "es_sales_index")
ingest_data_to_elasticsearch(feedback_collection, "es_feedback_index")
