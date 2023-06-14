import numpy as np
import pandas as pd
import qrcode
import uuid
from tkinter import * 
from tkinter import ttk
from customtkinter import * 


'''
colours
background: bedrock dark gray "#2E2E2E"
hover: bedrock green "#72c05b"
foreground/accent: bedrock orange "#f37367"
'''


class case:
    def __init__(self, brand, name, dimensions, cost, location):
        self.brand=brand
        self.name=name
        self.dimensions=dimensions
        self.cost=cost
        self.location=location
    def compile(self):
        fpath="requisites/cases.csv"
        data= pd.DataFrame({"Brand":self.brand, "Name":self.name, "dimensions":self.dimensions, "cost":self.cost, "location": self.location},index=[0])
        d_in=pd.read_csv(fpath)
        d_list=[d_in, data]
        d_out=pd.concat(d_list)
        d_out.to_csv(fpath, index=False)
