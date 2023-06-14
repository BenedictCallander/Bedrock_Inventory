import requests
from datetime import datetime, timedelta
from woocommerce import API

# WooCommerce API credentials
url = "https://bedrock-computers.co.uk/"
consumer_key = "ck_e63f2847761567231436732f8c753e392fd81614"
consumer_secret = "cs_d40131313ebeeb4e1bd8b8fb67e41afd487685cf"

# Calculate the date and time 24 hours ago
start_date = datetime.now() - timedelta(hours=24)

# Format the start date as required by the WooCommerce API
start_date_formatted = start_date.strftime('%Y-%m-%dT%H:%M:%S')

# Initialize the API object
wcapi = API(url=url, consumer_key=consumer_key, consumer_secret=consumer_secret, version="wc/v3")

# Prepare the query parameters
params = {
    'after': start_date_formatted
}

# Send the GET request to the WooCommerce API to retrieve orders
orders = wcapi.get("orders", params=params).json()

# Iterate over each order and extract the product names
for order in orders:
    order_id = order['id']
    line_items = order['line_items']

    # Extract the name of each product in the order
    product_names = [item['name'] for item in line_items]

    print(f"Order ID: {order_id}")
    print("Product Names:")
    for name in product_names:
        print(name)
    print('---')
