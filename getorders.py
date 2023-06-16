from tkinter import * 
from tkinter import ttk
from customtkinter import * 
import pandas as pd 
import numpy as np
import components as components 
import BCUTILS
from tkinter import messagebox
import sqlite3
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image
'''
colours
background: bedrock dark gray "#2E2E2E"
hover: bedrock green "#72c05b"
foreground/accent: bedrock orange "#f37367"
'''

'''
API Keys
Consumer key ck_e63f2847761567231436732f8c753e392fd81614
consumer secret cs_d40131313ebeeb4e1bd8b8fb67e41afd487685cf
'''




'''
Get ORDERS Psuedocode


press get orders button-> connect to API 
obtain all orders-> disect into individual components

if ? =? search ? -> return location and ID 
collect for all: summarise into single display -> print? 
scan individual barcode-> remove item from stock 
'''




def order_stock_depletion(order_id, product_ID):
    #order-> product_id
    additions=[1]
    sysinfo=pd.read_csv(f"requisites/systems/{product_ID}.csv")
    
    order_cpu=sysinfo['CPU']
    order_gpu=sysinfo['GPU']
    order_ram=sysinfo['RAM']+ additions['RAM']
    order_capacity=sysinfo['storage']+additions['storage']
    
    conn=sqlite3.connect("requisites/stock.db")
    c=conn.cursor()
    
    #
    #SQL remove query
    #
    
    conn.commit()
    conn.close()
    
