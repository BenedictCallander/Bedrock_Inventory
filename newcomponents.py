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
gen_4=["i7-4770", "i5-4670", "i5-4570", "i3-4370","i7-4790", "i5-4690", "i5-4590", "i3-4390"]
gen_5=["i7-5775C", "i5-5675C", "i5-5575R", "i3-5375C"]
gen_6=["i7-6700", "i5-6600", "i5-6500", "i3-6300","i7-6700K", "i5-6600K", "i5-6500T"]
gen_7=["i7-7700", "i5-7600", "i5-7500", "i3-7300","i7-7700K", "i5-7600K", "i5-7500T"]
gen_8=["i7-8700", "i5-8600", "i5-8500", "i3-8300","i7-8700K", "i5-8600K", "i5-8500T"]
gen_9=["i7-9700", "i5-9600", "i5-9500", "i3-9300","i7-9700K", "i5-9600K", "i5-9500T"]
gen_10=["i7-10700", "i5-10600", "i5-10500", "i3-10300","i7-10700K", "i5-10600K", "i5-10500T"]
gen_11=["i7-11700", "i5-11600", "i5-11500", "i3-11300","i7-11700K", "i5-11600K", "i5-11500T"]
gen_12=["i7-12700", "i5-12600", "i5-12500", "i3-12300","i7-12700K", "i5-12600K", "i5-12500T"]

class import_win:
    def componentwin():
        dbpath="requisites/stock.db"
        conn=sqlite3.connect(dbpath)
        
        #
        #CPU
        #
        
        gen_list=[gen_4, gen_5, gen_6, gen_7, gen_8, gen_9, gen_10, gen_11, gen_12]
        numlist=[4,5,6,7,8,9,10,11,12]
        
    win_import=CTkToplevel()
    
        
        