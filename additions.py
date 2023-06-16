import pandas as pd
from woocommerce import API

# WooCommerce API credentials
url = "https://bedrock-computers.co.uk/"
consumer_key = "ck_e63f2847761567231436732f8c753e392fd81614"
consumer_secret = "cs_d40131313ebeeb4e1bd8b8fb67e41afd487685cf"

# Initialize the API object
wcapi = API(url=url, consumer_key=consumer_key, consumer_secret=consumer_secret, version="wc/v3")

# Send the GET request to the WooCommerce API to retrieve all product attributes
attributes = wcapi.get("products/attributes").json()

# List to store the addition data
additions_data = []

# Iterate over each attribute to retrieve the attribute options
for attribute in attributes:
    attribute_id = attribute['id']
    attribute_name = attribute['name']

    # Send the GET request to the WooCommerce API to retrieve the attribute options
    attribute_options = wcapi.get(f"products/attributes/{attribute_id}/terms").json()

    # Iterate over each option to retrieve the option ID and name
    for option in attribute_options:
        option_id = option['id']
        option_name = option['name']

        # Add the option data to the additions_data list
        additions_data.append({'Attribute': attribute_name, 'Option ID': option_id, 'Option Name': option_name})

# Create a DataFrame from the additions_data list
df = pd.DataFrame(additions_data)

# Write the DataFrame to a CSV file
df.to_csv('additions_data.csv', index=False)
