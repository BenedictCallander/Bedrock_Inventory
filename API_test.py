import requests
from datetime import datetime, timedelta
from woocommerce import API
'''
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
    'after': start_date_formatted,
    'status': 'processing'
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
                addition_id=addition['id']
                addition_key = addition['key']
                addition_value = addition['value']

                # Exclude metadata with keys "_WCPA_order_meta_data" and "_wcpdf_regular_price"
                if addition_key not in ('_WCPA_order_meta_data', '_wcpdf_regular_price'):
                    print(f"{addition_id}:{addition_key}: {addition_value}")

        print('---')

'''


def extract_hdd_space(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

        # Search for the specific text string
        start_index = content.find("Extra HDD space: +")
        if start_index == -1:
            return None

        end_index = content.find("GB (£15.00)", start_index)
        if end_index == -1:
            return None

        # Extract the number from the text string
        number_text = content[start_index + len("Extra HDD space: +"):end_index]
        number = int(number_text)

        return number

# Provide the path to the text file
file_path = "orders/received/14747.txt"

# Call the function to extract the HDD space
hdd_space = extract_hdd_space(file_path)

if hdd_space is not None:
    print(f"The HDD space is: {hdd_space}GB")
else:
    print("The specific text string was not found in the file.")
    

def find_HDD_Logic(order_id):
    fpath=f"orders/received/{order_id}.txt"
    hard_addition=extract_hdd_space(fpath)
    if hard_addition is not None:
        stor_cond="Y"
        addition_storage=hard_addition
        return stor_cond, addition_storage
    else:
        stor_cond="N"
        return stor_cond

            

def extract_ram_space(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

        # Search for the specific text string
        start_index = content.find("Memory:")
        if start_index == -1:
            return None

        end_index = content.find("GB (£", start_index)
        if end_index == -1:
            return None

        # Extract the number from the text string
        number_text = content[start_index + len("Memory:"):end_index]
        number = int(number_text)

        return number
    
def find_ram_logic(order_id):
    fpath=f"orders/received/{order_id}.txt"
    ram=extract_ram_space(fpath)
    if ram is not None:
        ram_cond="Y"
        ram_value=ram
        return ram_cond,ram_value
    else:
        ram_cond="N"
        return ram_cond
    
def extract_ssd_size(fpath):
    with open(fpath, 'r') as file:
        content = file.read()

        # Search for the specific text string
        start_index = content.find("Solid state size: ")
        if start_index == -1:
            return None

        end_index = content.find("GB SSD", start_index)
        if end_index == -1:
            return None

        # Extract the number from the text string
        number_text = content[start_index + len("Solid state size:"):end_index]
        number = int(number_text)

        return number

def ssd_logic(order_id):
    fpath=f"orders/received/{order_id}.txt"
    ssd_storage=extract_ssd_size(fpath)
    if ssd_storage is not None:
        ssd_condition="Y"
        return ssd_condition, ssd_storage
    else:
        ssd_condition="N"
        return ssd_condition
    