import numpy as np 
import pandas as pd 
import BCUTILS
'''
'''


def shipping_class():
    r'''
    INPUTS: Order data
    
    PROCESS: checks weight and calculates necessary shiping class
    
    OUTPUTS: relevant shipping method
    
    '''
    

def item_location():
    r'''
    INPUTS: Item type/info
    
    PROCESS; checks storage dictionary to find location
    
    OUTPUTS: Item Location 
    
    '''


def ram_sticks(capacity):
    if capacity == 8:
        no_4 = 2
        no_8=0
    elif capacity==16:
        no_4=4 
        no_8=2
    elif capacity==12:
        no_4=3 
        no_4_var=1
        no_8=1
    return (no_4, no_8)
