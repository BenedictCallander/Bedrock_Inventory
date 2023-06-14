import numpy as np 
import pandas as pd 
from woocommerce import API 

'''
API Keys
Consumer key ck_e63f2847761567231436732f8c753e392fd81614
consumer secret cs_d40131313ebeeb4e1bd8b8fb67e41afd487685cf
'''

wcapi=API(url="https://bedrock-computers.co.uk/",
          consumer_key="ck_e63f2847761567231436732f8c753e392fd81614",
          consumer_secret="cs_d40131313ebeeb4e1bd8b8fb67e41afd487685cf")

order=wcapi.get("products/").json()
print(order)
