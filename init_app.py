from pymongo import MongoClient
from elasticsearch import Elasticsearch
import json

# Function to read data from a JSON file
def read_data_from_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Read data from JSON files into variables
user_data = read_data_from_file('data/user_data.json')
product_data = read_data_from_file('data/product_data.json')
sales_data = read_data_from_file('data/sales_data.json')
feedback_data = read_data_from_file('data/feedback_data.json')

# Set up a MongoDB client and connect to the local MongoDB instance
mongo_client = MongoClient("mongodb://localhost:27017/")
# Connect to the specific database 'ecommerce_db' in MongoDB
mongo_db = mongo_client["ecommerce_db"] 

# List of collection names to be used in MongoDB
collections = ["users", "products", "sales", "feedback"]
# Drop existing collections if they exist to start fresh
for collection in collections:
    mongo_db[collection].drop()

# Create references to each collection in MongoDB
users_collection = mongo_db["users"]
products_collection = mongo_db["products"]
sales_collection = mongo_db["sales"]
feedback_collection = mongo_db["feedback"]

# Function to insert data into a MongoDB collection
def insert_data_to_mongodb(collection, data):
    collection.insert_many(data)  # Insert the given data into the specified collection

# Insert data into respective MongoDB collections
insert_data_to_mongodb(users_collection, user_data)
insert_data_to_mongodb(products_collection, product_data)
insert_data_to_mongodb(sales_collection, sales_data)
insert_data_to_mongodb(feedback_collection, feedback_data)

# Set up an Elasticsearch client and connect to the local Elasticsearch instance
es_client = Elasticsearch("http://localhost:9200")

# List of index names to be used in Elasticsearch
indices = ["es_users_index", "es_products_index", "es_sales_index", "es_feedback_index"]

# Check if the indices exist in Elasticsearch and delete them if they do
if es_client.indices.exists(index="es_users_index"):
    es_client.indices.delete(index="es_users_index")
if es_client.indices.exists(index="es_products_index"):
    es_client.indices.delete(index="es_products_index")
if es_client.indices.exists(index="es_sales_index"):
    es_client.indices.delete(index="es_sales_index")
if es_client.indices.exists(index="es_feedback_index"):
    es_client.indices.delete(index="es_feedback_index")

# Function to ingest data from MongoDB to Elasticsearch
def ingest_data_to_elasticsearch(mongo_collection, es_index, explicit_mapping=None):
    if explicit_mapping:
        # Create Elasticsearch index with provided mapping if explicit_mapping is provided
        es_client.indices.create(index=es_index, body=explicit_mapping)

    for document in mongo_collection.find():
        # Remove MongoDB's '_id' field and use it as the Elasticsearch document ID
        mongo_id = str(document.pop("_id", None))
        # Index the document into Elasticsearch
        es_client.index(index=es_index, id=mongo_id, body=document)

# Define mappings for the Elasticsearch 'users' index
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

# Ingest data from MongoDB collections to corresponding Elasticsearch indices
ingest_data_to_elasticsearch(users_collection, "es_users_index", users_mapping)
ingest_data_to_elasticsearch(products_collection, "es_products_index")
ingest_data_to_elasticsearch(sales_collection, "es_sales_index")
ingest_data_to_elasticsearch(feedback_collection, "es_feedback_index")
