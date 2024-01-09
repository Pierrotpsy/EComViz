from faker import Faker
import random
import datetime
import json

# Initialize Faker library for generating fake data
fake = Faker()

# Function to generate fake user data
def generate_user_data(n):
    users = []  # List to store user data
    used_emails = set()  # Set to store and check for unique emails

    # Pre-defined list of cities with their latitude and longitude
    cities = [
      {"city": "New York", "lat": 40.7128, "lon": -74.0060},
      {"city": "Paris", "lat": 48.8566, "lon": 2.3522},
      {"city": "Tokyo", "lat": 35.6895, "lon": 139.6917},
      {"city": "Sydney", "lat": -33.8688, "lon": 151.2093},
      {"city": "Cape Town", "lat": -33.9249, "lon": 18.4241},
      {"city": "London", "lat": 51.5074, "lon": -0.1278},
      {"city": "Toronto", "lat": 43.65107, "lon": -79.347015},
      {"city": "Singapore", "lat": 1.3521, "lon": 103.8198},
      {"city": "Berlin", "lat": 52.5200, "lon": 13.4050},
      {"city": "Moscow", "lat": 55.7558, "lon": 37.6173},
      {"city": "Rio de Janeiro", "lat": -22.9068, "lon": -43.1729},
      {"city": "San Francisco", "lat": 37.7749, "lon": -122.4194},
      {"city": "Mumbai", "lat": 19.0760, "lon": 72.8777},
      {"city": "Shanghai", "lat": 31.2304, "lon": 121.4737},
      {"city": "Dubai", "lat": 25.276987, "lon": 55.296249},
      {"city": "Johannesburg", "lat": -26.2041, "lon": 28.0473},
      {"city": "Istanbul", "lat": 41.0082, "lon": 28.9784},
      {"city": "Mexico City", "lat": 19.4326, "lon": -99.1332},
      {"city": "Bangkok", "lat": 13.7563, "lon": 100.5018},
      {"city": "Hong Kong", "lat": 22.3193, "lon": 114.1694},
      {"city": "Los Angeles", "lat": 34.0522, "lon": -118.2437},
      {"city": "Chicago", "lat": 41.8781, "lon": -87.6298},
      {"city": "Houston", "lat": 29.7604, "lon": -95.3698},
      {"city": "Phoenix", "lat": 33.4484, "lon": -112.0740},
      {"city": "Philadelphia", "lat": 39.9526, "lon": -75.1652},
      {"city": "San Antonio", "lat": 29.4241, "lon": -98.4936},
      {"city": "San Diego", "lat": 32.7157, "lon": -117.1611},
      {"city": "Dallas", "lat": 32.7767, "lon": -96.7970},
      {"city": "San Jose", "lat": 37.3382, "lon": -121.8863},
      {"city": "Austin", "lat": 30.2672, "lon": -97.7431},
      {"city": "Jacksonville", "lat": 30.3322, "lon": -81.6557},
      {"city": "Fort Worth", "lat": 32.7555, "lon": -97.3308},
      {"city": "Columbus", "lat": 39.9612, "lon": -82.9988},
      {"city": "Charlotte", "lat": 35.2271, "lon": -80.8431},
      {"city": "Indianapolis", "lat": 39.7684, "lon": -86.1581},
      {"city": "Seattle", "lat": 47.6062, "lon": -122.3321},
      {"city": "Denver", "lat": 39.7392, "lon": -104.9903},
      {"city": "Washington D.C.", "lat": 38.9072, "lon": -77.0369},
      {"city": "Boston", "lat": 42.3601, "lon": -71.0589},
      {"city": "El Paso", "lat": 31.7619, "lon": -106.4850},
      {"city": "Nashville", "lat": 36.1627, "lon": -86.7816},
      {"city": "Detroit", "lat": 42.3314, "lon": -83.0458},
      {"city": "Oklahoma City", "lat": 35.4676, "lon": -97.5164},
      {"city": "Portland", "lat": 45.5051, "lon": -122.6750},
      {"city": "Las Vegas", "lat": 36.1699, "lon": -115.1398},
      {"city": "Memphis", "lat": 35.1495, "lon": -90.0490},
      {"city": "Louisville", "lat": 38.2527, "lon": -85.7585},
      {"city": "Baltimore", "lat": 39.2904, "lon": -76.6122},
      {"city": "Milwaukee", "lat": 43.0389, "lon": -87.9065},
      {"city": "Albuquerque", "lat": 35.0844, "lon": -106.6504},
      {"city": "Tucson", "lat": 32.2226, "lon": -110.9747},
      {"city": "Fresno", "lat": 36.7378, "lon": -119.7871},
      {"city": "Sacramento", "lat": 38.5816, "lon": -121.4944},
      {"city": "Kansas City", "lat": 39.0997, "lon": -94.5786},
      {"city": "Long Beach", "lat": 33.7701, "lon": -118.1937},
      {"city": "Mesa", "lat": 33.4152, "lon": -111.8315},
      {"city": "Atlanta", "lat": 33.7490, "lon": -84.3880},
      {"city": "Colorado Springs", "lat": 38.8339, "lon": -104.8214},
      {"city": "Virginia Beach", "lat": 36.8529, "lon": -75.9780},
      {"city": "Raleigh", "lat": 35.7796, "lon": -78.6382},
      {"city": "Omaha", "lat": 41.2565, "lon": -95.9345},
      {"city": "Miami", "lat": 25.7617, "lon": -80.1918},
      {"city": "Oakland", "lat": 37.8044, "lon": -122.2712},
      {"city": "Minneapolis", "lat": 44.9778, "lon": -93.2650},
      {"city": "Tulsa", "lat": 36.15398, "lon": -95.992775},
      {"city": "Wichita", "lat": 37.6872, "lon": -97.3301},
      {"city": "New Orleans", "lat": 29.9511, "lon": -90.0715},
      {"city": "Arlington", "lat": 32.7357, "lon": -97.1081},
      {"city": "Bakersfield", "lat": 35.3733, "lon": -119.0187},
      {"city": "Cleveland", "lat": 41.4993, "lon": -81.6944},
      {"city": "Aurora", "lat": 39.7294, "lon": -104.8319},
      {"city": "Anaheim", "lat": 33.8366, "lon": -117.9143},
      {"city": "Honolulu", "lat": 21.3069, "lon": -157.8583},
      {"city": "Santa Ana", "lat": 33.7455, "lon": -117.8677},
      {"city": "Riverside", "lat": 33.9806, "lon": -117.3755}
    ]

    # Generate user data until the desired number of users is reached
    while len(users) < n:
        email = fake.email()  # Generate a random email
        # Ensure the email is unique
        if email not in used_emails:
            used_emails.add(email)
            chosen_city = random.choice(cities)  # Randomly pick a city from the list
            address = fake.address()  # Generate a random address
            formatted_address = f"{address}, {chosen_city['city']}"
            # Create a geojson object for the user's location
            geojson = {
                "type": "Point",
                "coordinates": [chosen_city["lon"], chosen_city["lat"]]
            }
            # Create a user dictionary with various attributes
            user = {
                "user_id": fake.uuid4(),
                "name": fake.name(),
                "email": email,
                "address": formatted_address,
                "join_date": fake.date_this_decade().isoformat(),
                "location": geojson
            }
            users.append(user)  # Add the user to the list of users

    return users

# Function to generate fake product data
def generate_product_data(n):
    products = []  # List to store product data
    used_names = set()  # Set to store and check for unique product names
    # Define product categories and their associated features
    categories = {
      "Electronics": ["high-performance", "energy-efficient", "user-friendly", "compact", "innovative design"],
      "Accessories": ["durable", "stylish", "lightweight", "versatile", "premium quality"],
      "Wearable Tech": ["fitness tracking", "sleep monitoring", "water-resistant", "touchscreen", "heart rate sensor"],
      "Photography": ["high resolution", "optical zoom", "wide aperture", "image stabilization", "4K video recording"],
      "Home Appliances": ["energy-saving", "low noise", "smart technology", "easy to use", "modern design"]
    }

    # Generate product data until the desired number of products is reached
    while len(products) < n:
        name = fake.word().title() + ' ' + random.choice(["Laptop", "Smartphone", "Headphones", "Camera", "Watch"])
        # Ensure the product name is unique
        if name not in used_names:
            used_names.add(name)
            category = random.choice(list(categories.keys()))  # Randomly pick a category
            description_phrases = random.sample(categories[category], 3)  # Select 3 random features
            description = f"This {category.lower()} product offers {', '.join(description_phrases)}."
            # Create a product dictionary with various attributes
            product = {
                "product_id": fake.uuid4(),
                "name": name,
                "description": description,
                "price": round(random.uniform(50, 1500), 2),
                "category": category
            }
            products.append(product)  # Add the product to the list of products

    return products

# Function to generate fake sales data
def generate_sales_data(n, users, product_ids):
    sales = []  # List to store sales data

    for _ in range(n):
        user = random.choice(users)  # Randomly pick a user
        user_join_date = datetime.datetime.strptime(user['join_date'], '%Y-%m-%d')
        # Generate a sale date that is after the user's join date
        sale_date = fake.date_between_dates(date_start=user_join_date, date_end=datetime.date(2024, 1, 6)).isoformat()
        # Create a sale dictionary with various attributes
        sale = {
            "sale_id": fake.uuid4(),
            "user_id": user['user_id'],
            "product_id": random.choice(product_ids),
            "quantity": random.randint(1, 10),
            "sale_date": sale_date
        }
        sales.append(sale)  # Add the sale to the list of sales

    return sales

# Function to generate fake feedback data
def generate_feedback_data(n, users, product_ids):
    feedbacks = []  # List to store feedback data
    # Define adjectives categorized by sentiment
    positive_adjectives = ['excellent', 'amazing', 'incredible', 'exceptional', 'fantastic']
    neutral_adjectives = ['satisfactory', 'mediocre']
    negative_adjectives = ['poor', 'disappointing', 'subpar']
    # Templates for feedback comments
    comment_templates = [
      "This product is absolutely {}.",
      "I found the product to be {}.",
      "My experience with this product was {}.",
      "It's a {} product.",
      "Overall, the product is {}."
    ]

    while len(feedbacks) < n:
        # Randomly choose a sentiment category
        sentiment_choice = random.choice(['positive', 'neutral', 'negative'])
        # Assign adjectives and ratings based on sentiment
        if sentiment_choice == 'positive':
            adjective = random.choice(positive_adjectives)
            rating = random.randint(4, 5)  # Higher rating for positive feedback
        elif sentiment_choice == 'neutral':
            adjective = random.choice(neutral_adjectives)
            rating = random.randint(2, 3)  # Moderate rating for neutral feedback
        else:  # negative
            adjective = random.choice(negative_adjectives)
            rating = random.randint(0, 1)  # Lower rating for negative feedback

        comment_template = random.choice(comment_templates)
        comment = comment_template.format(adjective)
        # Choose a user and their join date
        user = random.choice(users)
        user_join_date = datetime.datetime.strptime(user['join_date'], '%Y-%m-%d')
        # Generate a feedback date that is after the user's join date
        feedback_date = fake.date_between_dates(date_start=user_join_date, date_end=datetime.date(2024, 1, 6)).isoformat()
        # Create a feedback dictionary with various attributes
        feedback = {
            "feedback_id": fake.uuid4(),
            "user_id": user['user_id'],
            "product_id": random.choice(product_ids),
            "rating": rating,
            "comment": comment,
            "feedback_date": feedback_date
        }
        feedbacks.append(feedback)  # Add the feedback to the list of feedbacks

    return feedbacks

# Generate data with specific counts
num_users = 1000
num_products = 500
num_sales = 20000
num_feedbacks = 1000

# Generate user, product, sales, and feedback data
user_data = generate_user_data(num_users)
product_data = generate_product_data(num_products)
# Assuming the existence of a product_ids list
sales_data = generate_sales_data(num_sales, user_data, [product['product_id'] for product in product_data])
feedback_data = generate_feedback_data(num_feedbacks, user_data, [product['product_id'] for product in product_data])

# Function to write data to a JSON file
def write_data_to_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)  # Write data to file in JSON format with indentation

# Write generated data to respective JSON files
write_data_to_file(user_data, 'user_data.json')
write_data_to_file(product_data, 'product_data.json')
write_data_to_file(sales_data, 'sales_data.json')
write_data_to_file(feedback_data, 'feedback_data.json')
