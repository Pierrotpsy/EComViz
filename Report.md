# E-Commerce Analytics Web App Project Report

By Maxime Merlin
***

## Project Aim
This project's goal was to create an app using MongoDB, Elasticsearch, and Kibana, showcasing what these technologies are capable of.

## Overview

### Choosing E-Commerce
I chose the e-commerce sector for this project because it's rich in data. Designing a database for a small e-commerce site is relatively straightforward, and it was a great opportunity to create some mock data.

### Data Generation
Without any initial data, I turned to the `Faker` Python library to generate what I needed. The challenge was creating realistic product names and reviews, which I managed with some clever templates and word lists.

This method of generating data avoided the complexities of cleaning existing datasets. It also allowed me to flexibly demonstrate MongoDB and Elasticsearch features. Working with synthetic data was a practical experience, mirroring a common practice in development.

Though the data was fabricated, it was structured realistically for an e-commerce context. This means the data analysis might not directly apply, but the visualizations and data relations are very much real-world applicable.

### The App

#### Tech Stack
Here’s what I used to build the app:
- **Frontend**: Basic HTML, CSS, JavaScript, with Chart.js and DataTables for charting.
- **Backend**: Flask for the web framework, MongoDB, and Elasticsearch.
- **Data Visualization**: Kibana for in-depth analytics.

The use of HTML, CSS, and JavaScript was kept straightforward as the focus was more on backend technologies. However, incorporating JavaScript for additional charting provided a nice touch.

Flask, a Python framework, was central to the app, connecting the dots between MongoDB, Elasticsearch, and the app's functionality.

#### Features

##### Data Visualization
I created a separate webpage for each data collection - Users, Products, Sales, Feedbacks. Each page not only allows for data viewing but also displays simple charts using JavaScript. DataTables enhance data viewing and searchability.

##### Universal Search
Elasticsearch's search capabilities are harnessed in a universal search feature, allowing searches across all data collections, which are in sync with MongoDB and Elasticsearch.

##### Data Input
While data deletion or editing wasn't included, I did add a feature for data input. Adding an item updates both the MongoDB collection and the Elasticsearch index, affecting the data collection webpages, the search function, and the Kibana dashboard.

##### Kibana Dashboard
The data mirrored in Elasticsearch enabled the integration of a Kibana dashboard in the app, updating in real-time with the Elasticsearch indices. Initially, it features 10 graphs, but this is easily expandable.

#### Demo
Here's a brief video showcasing the app's features:

![demo](https://github.com/Pierrotpsy/EComViz/blob/main/images/EComViz_demo.webm)
## Technical Choices Explained

### Flask
- **Role**: Flask was used as the backend framework, ideal for integrating MongoDB and Elasticsearch.
- **Endpoints**: Flask manages various endpoints like `/users`, `/products`, etc., serving HTML templates and MongoDB data in JSON format.

### MongoDB
- **Usage**: MongoDB serves as the primary database, storing data on users, products, sales, and feedback.
- **Reason for Choosing**: Its NoSQL nature provides the necessary flexibility and scalability for dynamic e-commerce data. In my specific usage of it, its NoSQL nature also allowed for iterative development of the data generation script.

### Elasticsearch
- **Usage**: Elasticsearch enhances the app's search functionality.
- **Reason for Choosing**: Its fast, real-time search capability is crucial for managing the large data volumes typical in e-commerce platforms. I didn't put it to the test with my usage of it since I have at most 20 000 items in any collection, which even MongoDB can easily handle, but we can imagine that an e-commerce platform would generate enormous amounts of data, which Elasticsearch would be capable of managing.
