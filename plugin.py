import woocomerce
import numpy as np 
import pandas as pd 


class order:
    def __init__(self, order_ID, order_case, order_CPU, order_GPU, order_PSU, order_RAM, order_accessories):
        self.order_ID=order_ID
        self.order_case=order_case
        self.order_CPU=order_CPU
        self.order_GPU=order_GPU
        self.order_PSU=order_PSU
        self.order_RAM=order_RAM
        self.order_accessories=order_accessories

    def printlabel():
        return print("LABEL")
    
    def showscreen():
        '''
        Open Dedicated order window showing info and functional buttons (scan gpu etc)
        
        '''
        return 0

    def order_status():
        '''
        Buttons to indicate order status and print shipping 
        '''
        
        return 0
    
    