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
import uuid
from PIL import Image


'''
colours
background: bedrock dark gray "#2E2E2E"
hover: bedrock green "#72c05b"
foreground/accent: bedrock orange "#f37367"
'''



'''
app=CTk()
tabview = CTkTabview(master=app)
tabview.pack(padx=20, pady=20)

tabview.add("tab 1")  # add tab at the end
tabview.add("tab 2")  # add tab at the end
tabview.set("tab 2")  # set currently visible tab

button = CTkButton(master=tabview.tab("tab 1"))
button.pack(padx=20, pady=20)

app.mainloop()
'''


class view_window:
    def view():
        viewsubwin=CTkToplevel()
        viewsubwin.configure(fg_color="#2E2E2E")
        viewsubwin.geometry("1280x720")
        
        
        tabview=CTkTabview(master=viewsubwin)
        tabview.pack(padx=20,pady=20)
        tab1=tabview.add("CPU")
        tab2=tabview.add("GPU")
        tab3=tabview.add("PSU")
        tabview.configure(fg_color="#f37367",
                          border_color='black',
                          segmented_button_fg_color="#2E2E2E",
                          segmented_button_unselected_color="#fcba03",
                          segmented_button_selected_color="#72c05b")
        
        tabs=[tab1,tab2,tab3]
        for tab in tabs:
            tab.configure(fg_color="#2E2E2E")
        
        

        
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",background="#2a2d2e",foreground="white",rowheight=25,fieldbackground="#343638",bordercolor="#343638",borderwidth=0)
        style.map('Treeview', background=[('selected', '#22559b')])
        style.configure("Treeview.Heading",background="#565b5e",foreground="white",relief="flat")
        style.map("Treeview.Heading",background=[('active', '#3484F0')])

        #
        #GPU
        #
        gpu_title_label=CTkLabel(tab2, text="GPU STOCK", font=("Berlin",20), text_color="#f37367")
        gpu_title_label.grid(row=0, column=0, padx=20, pady=20)
        #
        #read data
        #
        df_gpu= pd.read_csv("requisites/gpu.csv")
        gpu_list_brand= list(df_gpu['BRAND'])
        gpu_list_name=list(df_gpu['NAME'])
        gpu_list_loc=list(df_gpu['Location'])
        gpu_list_cost=list(df_gpu['Cost'])
        gpu_list_id=list(df_gpu['ID'])
        #
        #plot tree
        #
        gpu_headings = ("Brand", "Name", "Location", "Cost", "ID")
        gpu_tree = ttk.Treeview(tab2, columns=gpu_headings, show='headings')
        gpu_tree.grid(row=1, column=0, padx=20, pady=20)
        for heading in gpu_headings:
            gpu_tree.heading(heading, text=heading)
        for brand, name,location,cost,id in zip(gpu_list_brand, gpu_list_name,gpu_list_loc,gpu_list_cost,gpu_list_id):
            gpu_tree.insert('', 'end', values=(brand, name, location,cost,id))

        #
        #
        #

        #
        #CPU
        #

        df_cpu= pd.read_csv("requisites/cpu.csv")
        cpu_list_brand= list(df_cpu['BRAND'])
        cpu_list_name=list(df_cpu['NAME'])
        cpu_list_id=list(df_cpu['ID'])
        cpu_list_loc=list(df_cpu['Location'])

        cpu_title_label=CTkLabel(tab1, text="CPU STOCK", font=("Berlin",20), text_color="#f37367")
        cpu_title_label.grid(row=0, column=0, padx=20, pady=20)

        cpu_headings= ("Brand","Name","Location", "ID")
        cpu_tree=ttk.Treeview(tab1,columns=cpu_headings, show='headings')
        cpu_tree.grid(row=1, column=0,pady=20,padx=20)
        for heading in cpu_headings:
            cpu_tree.heading(heading, text=heading)
        
        for brand,name,location, id in zip(cpu_list_brand, cpu_list_name,cpu_list_loc, cpu_list_id):
            cpu_tree.insert('', 'end', values=(brand,name,location,id))

        #
        #
        #
        def sort_column(tree, col, reverse):
            data = [(tree.set(child, col), child) for child in tree.get_children("")]
            data.sort(key=lambda x: int(x[0]), reverse=reverse)
            for index, (value, child) in enumerate(data):
                tree.move(child, "", index)
            tree.heading(col, command=lambda: sort_column(tree, col, not reverse))
        
        #
        #psu_
        #
        conn=sqlite3.connect("requisites/stock.db")
        c = conn.cursor()
        c.execute('SELECT * from psu')
        datapsu = c.fetchall()
        psu_title_label=CTkLabel(tab3, text="PSU STOCK", font=("Berlin",20), text_color="#f37367")
        psu_title_label.grid(row=0, column=0, padx=20, pady=20)
        psu_headings = ("Power", "Price", "Stock")
        psu_tree = ttk.Treeview(tab3, columns=psu_headings, show='headings')
        psu_tree.grid(row=1, column=0,padx=20,pady=20)

        for heading in psu_headings:
            psu_tree.heading(heading, text=heading, command=lambda col=heading: sort_column(psu_tree, col, False))
        for i, (power, price, stock) in enumerate(datapsu):
            psu_tree.insert('', 'end', values=(power, price, stock))

            sum=0
        power,price,stock= zip(*datapsu)

        for i in range(len(power)):
            value=price[i]*stock[i]
            sum=sum+value
        total=CTkLabel(tab3,text=f'Total Value: £{sum}',font=("Berlin", 20),text_color="#f37367")
        total.grid(row=3, column=0,padx=20,pady=20)

        plot_title= CTkLabel(tab3, text="PSU Stock History", text_color="#f37367", font=("Berlin", 30))
        plot_title.grid(row=0,column=5,padx=20,pady=20)
        fpath="requisites/temp_psu.png"
        plot_image=CTkImage(light_image=Image.open(fpath),size=(500,300))
        img_label=CTkLabel(tab3, image=plot_image, text='')
        img_label.grid(row=1,column=5,padx=20,pady=20)

        conn.commit()
        conn.close()
        
        viewsubwin.mainloop()
        

view_window.view()
        