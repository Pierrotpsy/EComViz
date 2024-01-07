# E-Commerce Analytics Webapp Project Report

## Objective
The E-Commerce Analytics Webapp is designed to leverage MongoDB and Elasticsearch for efficient data storage, management, and advanced search capabilities in an e-commerce context.

## Key Components & Justification

### MongoDB
- **Usage**: MongoDB is utilized as the primary database for storing user, product, sales, and feedback data.
- **Justification**: Its NoSQL nature allows for flexible data models and scalability, making it ideal for handling varied and evolving e-commerce data.

### Elasticsearch
- **Usage**: Elasticsearch is integrated for advanced search functionality across the dataset.
- **Justification**: It provides fast, real-time search capabilities and is particularly efficient in handling large volumes of data, essential for e-commerce platforms.

### Flask Web Application
- **Backend**: The application is developed using Flask, a Python web framework, facilitating easy integration with MongoDB and Elasticsearch.
- **Endpoints**: Various endpoints (e.g., `/users`, `/products`, `/sales`, `/feedback`) render respective HTML templates and serve JSON data from MongoDB.

### Data Visualization & Analytics
- **Kibana**: Integrated for creating dynamic, real-time data visualizations and dashboards.
- **Templates**: HTML templates (`dashboard.html`, `feedback.html`, `products.html`, `sales.html`, `users.html`) include elements like tables and charts for displaying data.

## Technical Stack
- **Frontend**: HTML, CSS, JavaScript, and visualization libraries (Chart.js, DataTables).
- **Backend**: Flask, MongoDB, Elasticsearch.
- **Data Visualization**: Kibana for advanced analytics.

## Data Management & Integration
- **Data Generation**: `generate_data.py` script for generating fake data.
- **MongoDB Setup**: Data is ingested into MongoDB collections (`users`, `products`, `sales`, `feedback`).
- **Elasticsearch Integration**: Data from MongoDB is indexed in Elasticsearch for efficient searching.

## Application Features
- **Interactive Web Interface**: Users can view and interact with e-commerce data through various web pages.
- **Data API Endpoints**: Flask routes (`/api/sales`, `/api/users`, `/api/feedback`, `/api/products`) provide JSON data for frontend consumption.
- **Search Functionality**: A universal search feature, powered by Elasticsearch, allows for searching across different datasets.

## Conclusion
This project effectively demonstrates the use of MongoDB for NoSQL data management and Elasticsearch for advanced search capabilities in an e-commerce context. The integration with a Flask web application and Kibana dashboards makes it a comprehensive solution for e-commerce analytics.
