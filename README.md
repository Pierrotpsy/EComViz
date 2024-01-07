# E-Commerce Analytics Dashboard

This Flask application provides an interface for managing and analyzing e-commerce data, integrating MongoDB for data storage and Elasticsearch for search and analytics.

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
git clone https://github.com/your-repository/ecommerce-dashboard.git
cd ecommerce-dashboard
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