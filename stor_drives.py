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

class hdd:
    def __init__(self, capacity, unit_cost, location):
        self.storage=capacity
        self.unit_cost=unit_cost
        self.location=location
        self.id=uuid.uuid4()

    def add(self):
        fpath="requisites/hdd.csv"
        addvar=pd.DataFrame({"Capacity": self.storage, "Cost": self.unit_cost, "Location": self.location, "ID":self.id}, index=[0])
        data_in= pd.read_csv(fpath)
        dlist=[data_in, addvar]
        dout=pd.concat(dlist)
        dout.to_csv(fpath, index=False)
class ssd:
    def __init__(self, capacity, unit_cost,location):
        self.storage=capacity
        self.unit_cost=unit_cost
        self.id=uuid.uuid4()
        self.location=location
    def add(self):
        fpath="requisites/ssd.csv"
        addvar=pd.DataFrame({"Capacity": self.storage, "Cost": self.unit_cost, "Location": self.location, "ID":self.id}, index=[0])
        data_in= pd.read_csv(fpath)
        dlist=[data_in, addvar]
        dout=pd.concat(dlist)
        dout.to_csv(fpath, index=False)


class in_win:
    def stor_win():
        subwin_storage=CTkToplevel()
        subwin_storage.configure(fg_color="#2E2E2E")
        subwin_storage.title("BEDROCK:STORAGE IMPORT")
        
        maintitle=CTkLabel(subwin_storage, text="Storage Import", font=("Berlin",30), text_color="#f37367")
        maintitle.grid(row=0,column=0, columnspan=2,padx=20,pady=20)
        hddframe=CTkFrame(subwin_storage,border_width=5, border_color="black")
        ssdframe=CTkFrame(subwin_storage,border_width=5, border_color="black")
        hddframe.configure(fg_color="#2E2E2E")
        ssdframe.configure(fg_color="#2E2E2E")

        hddframe.grid(row=1,column=0,padx=20,pady=20)
        ssdframe.grid(row=1,column=1,padx=20,pady=20)
        
        
        
        #
        #HDD frame
        #
        hd_title=CTkLabel(hddframe, text="HDD", font=("Berlin",30), text_color="#f37367")
        hd_title.grid(row=0,column=0, columnspan=2,padx=20,pady=20)
        hd_label_capacity=CTkLabel(hddframe, text="Capacity (GB):", font=("Berlin", 20), text_color="#f37367")
        hd_label_cost=CTkLabel(hddframe, text="Cost (£):", font=("Berlin", 20), text_color="#f37367")
        hd_label_location=CTkLabel(hddframe, text="Location:", font=("Berlin", 20), text_color="#f37367")
        hd_label_quantity=CTkLabel(hddframe, text="Quantity:", font=("Berlin", 20), text_color="#f37367")
        
        
        hd_entry_capacity=CTkEntry(hddframe, width=200)
        hd_entry_cost=CTkEntry(hddframe, width=200)
        hd_entry_location=CTkEntry(hddframe, width=200)
        hd_entry_quantity=CTkEntry(hddframe, width=200)
        
        
        hd_label_capacity.grid(row=1,column=0,padx=20,pady=20)
        hd_entry_capacity.grid(row=1,column=1,padx=20,pady=20)
        
        hd_label_cost.grid(row=2,column=0,padx=20,pady=20)
        hd_entry_cost.grid(row=2,column=1,padx=20,pady=20)
        
        hd_label_location.grid(row=3, column=0,padx=20,pady=20)
        hd_entry_location.grid(row=3,column=1,padx=20,pady=20)
        
        hd_label_quantity.grid(row=4,column=0,padx=20,pady=20)
        hd_entry_quantity.grid(row=4, column=1,padx=20,pady=20)
        
        def hd_buttonfunc():
            n=int(hd_entry_quantity.get())
            for _ in range(n):
                add=hdd(int(hd_entry_capacity.get()), int(hd_entry_cost.get()), hd_entry_location.get())
                add.add()
            hd_entry_capacity.delete(0,END)
            hd_entry_cost.delete(0,END)
            hd_entry_location.delete(0,END)
            hd_entry_quantity.delete(0,END)
        hd_button=CTkButton(hddframe,text="Submit",width=150, height=75, fg_color="#f37367", hover_color= "#72c05b", corner_radius=30,command=hd_buttonfunc)
        hd_button.grid(row=5,column=1,padx=20,pady=20)
        

        #
        #SSD Frame
        #
        
        sd_title=CTkLabel(ssdframe, text="SSD", font=("Berlin",30), text_color="#f37367")
        sd_title.grid(row=0,column=0, columnspan=2,padx=20,pady=20)
        
        
        sd_label_capacity=CTkLabel(ssdframe, text="Capacity (GB):", font=("Berlin", 20), text_color="#f37367")
        sd_label_cost=CTkLabel(ssdframe, text="Cost (£):", font=("Berlin", 20), text_color="#f37367")
        sd_label_location=CTkLabel(ssdframe, text="Location:", font=("Berlin", 20), text_color="#f37367")
        sd_label_quantity=CTkLabel(ssdframe, text="Quantity:", font=("Berlin", 20), text_color="#f37367")
        
        
        sd_entry_capacity=CTkEntry(ssdframe, width=200)
        sd_entry_cost=CTkEntry(ssdframe, width=200)
        sd_entry_location=CTkEntry(ssdframe, width=200)
        sd_entry_quantity=CTkEntry(ssdframe, width=200)
        
        
        sd_label_capacity.grid(row=1,column=0,padx=20,pady=20)
        sd_entry_capacity.grid(row=1,column=1,padx=20,pady=20)
        
        sd_label_cost.grid(row=2,column=0,padx=20,pady=20)
        sd_entry_cost.grid(row=2,column=1,padx=20,pady=20)
        
        sd_label_location.grid(row=3, column=0,padx=20,pady=20)
        sd_entry_location.grid(row=3,column=1,padx=20,pady=20)
        
        sd_label_quantity.grid(row=4,column=0,padx=20,pady=20)
        sd_entry_quantity.grid(row=4, column=1,padx=20,pady=20)
        
        def sd_buttonfunc():
            n=int(sd_entry_quantity.get())
            for _ in range(n):
                add=ssd(int(sd_entry_capacity.get()), int(sd_entry_cost.get()), sd_entry_location.get())
                add.add()
            sd_entry_capacity.delete(0,END)
            sd_entry_cost.delete(0,END)
            sd_entry_location.delete(0,END)
            sd_entry_quantity.delete(0,END)
        sd_button=CTkButton(ssdframe,text="Submit",width=150, height=75, fg_color="#f37367", hover_color= "#72c05b", corner_radius=30,command=sd_buttonfunc)
        sd_button.grid(row=5,column=1,padx=20,pady=20)
        subwin_storage.mainloop()
    
        
 
    
    
        