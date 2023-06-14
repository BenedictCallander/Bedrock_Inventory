import requests
from datetime import datetime, timedelta
from woocommerce import API

# WooCommerce API credentials
url = "https://bedrock-computers.co.uk/"
consumer_key = "ck_e63f2847761567231436732f8c753e392fd81614"
consumer_secret = "cs_d40131313ebeeb4e1bd8b8fb67e41afd487685cf"

# Calculate the date and time 24 hours ago
start_date = datetime.now() - timedelta(hours=72)

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

# Iterate over each order and extract the products and additions
for order in orders:
    order_id = order['id']
    line_items = order['line_items']

    print(f"Order ID: {order_id}")
    for item in line_items:
        product_name = item['name']
        variations = item.get('variations', [])
        additions = item.get('meta_data', [])

        print("Product Name:", product_name)

        if variations:
            print("Variations:")
            for variation in variations:
                variation_id = variation['variation_id']
                print(f"Variation ID: {variation_id}")

        if additions:
            print("Additions:")
            for addition in additions:
                addition_key = addition['key']
                addition_value = addition['value']

                # Exclude metadata with key "_WCPA_order_meta_data"
                if addition_key != '_WCPA_order_meta_data' and addition_key != '_wcpdf_regular_price':
                    print(f"{addition_key}: {addition_value}")

        print('---')
