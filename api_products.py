import requests
from woocommerce import API

# WooCommerce API credentials
url = "https://bedrock-computers.co.uk/"
consumer_key = "ck_e63f2847761567231436732f8c753e392fd81614"
consumer_secret = "cs_d40131313ebeeb4e1bd8b8fb67e41afd487685cf"

# Initialize the API object
wcapi = API(url=url, consumer_key=consumer_key, consumer_secret=consumer_secret, version="wc/v3")

# Send the GET request to the WooCommerce API to retrieve all products
page = 1
products = []

while True:
    response = wcapi.get("products", params={"per_page": 100, "page": page})
    if response.status_code != 200:
        print(f"Failed to fetch products. Error: {response.content}")
        break

    current_products = response.json()
    if not current_products:
        break

    products.extend(current_products)
    page += 1

# Iterate over each product and extract the data
for product in products:
    product_id = product['id']
    product_name = product['name']
    variations = product.get('variations', [])

    print(f"Product ID: {product_id}")
    print(f"Product Name: {product_name}")

    if variations:
        print("Variations:")
        for variation in variations:
            variation_id = variation['id']
            variation_name = variation['name']
            print(f"Variation ID: {variation_id}")
            print(f"Variation Name: {variation_name}")

    print('---')
