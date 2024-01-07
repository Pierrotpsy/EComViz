# E-Commerce Analytics Webapp

This Flask application provides an interface for managing and analyzing e-commerce data, integrating MongoDB for data storage and Elasticsearch for search and analytics. A Kibana dashboard is linked to the Elasticsearch instance for analytics purposes.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6+
- MongoDB 4.4+
- Elasticsearch 7.10+
- Flask 1.1+
- Kibana

## Installation

Clone the repository:

```bash
git clone https://github.com/Pierrotpsy/EComViz.git
cd EComViz
```

Install the required Python packages:
```bash
pip install -r requirements.txt
```

## Configuration
Ensure MongoDB and Elasticsearch services are running. Update the python scripts to point to the correct instances if needed.

Then, you'll need to populate your databases by running the `init-app.py` script. This will use the four data file present in the `/data` directory.
```bash
python3 init-app.py
```

Alternatively, you can choose to generate new data by running the `generate-data.py` script:
```bash
python3 data/generate-data.py
```

## Running the Application
To run the Flask application:
```bash
python3 app.py
```
Then open a web browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/). You should see the web app and be able to navigate through the different pages.

## Setting up the Kibana Dashboard

After the data has been properly ingested by Elasticsearch, you can set up your own Kibana dashboard.  
Go to [http://localhost:5601/app/management/kibana/indexPatterns](http://localhost:5601/app/management/kibana/indexPatterns) and add all the index patterns as shown below:  
![index_patterns.png]()
For all of them, be sure to specify a time field if one is available.
Then, go to [http://localhost:5601/app/dashboards#/create?_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-5y,to:now))](http://localhost:5601/app/dashboards#/create?_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-5y,to:now))) and add as many visualizations as you want. For the data I used, here are the graphs I chose:  
  
  1. User Join Date Over Time (es_users*) 
![user_join_date_over_time.png]()
  2. Product Categories Distribution (es_products*)
![product_categories.png]()
  3. Product Price Range Distribution per Category (es_products*)
![product_categories.png]()
  4. Sales Over Time (es_sales*)
![sales_over_time.png]()
  5. Top Selling Products (es_sales*)
![top_selling_products.png]()
  6. Average Rating per Product (es_feedback*)
![average_rating_per_product.png]()
  7. Number Of Feeback Over Time (es_feedback*)
![number_of_feedbacks.png]()
  8. Average Rating Over Time (es_feedback*)
![average_rating_over_time.png]()
  9. User Location (es_users*)
![user_location.png]()
  10. Sales Quantity vs Feedback Rating Over Time (es_sales* & es_feedback*)
![sales_vs_feedback.png]()

Then, save the dashboard and click on Share>Embed Code. Select 'Saved Object', 'Query', 'Time Filter' and 'Filter Bar', then 'Copy iFrame Code'. Now, open `templates/dashboard.html` and change the existing iFrame link with the one you have. Be careful only to edit the link and not the rest of the HTML code. You should now be able to access your Kibana Dashboard from the webapp.