from tkinter import messagebox
import pandas as pd 
import openpyxl
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import *
from tkinter.messagebox import showinfo
master = Tk()
master.title("BRAND SORT")

canvas = Canvas(master , height=600 , width=900)
canvas.pack()
frame_genel = Frame(master , bg="#000000")
frame_genel.place(relx = 0 , rely = 0 ,  relwidth = 1 , relheight = 1)
def cagir2():
    a = fd.askopenfilename()
    pd_file =pd.read_excel(a)
    
    pd_file['Brand'] = pd_file['Brand'].astype(str)
    pd_work = pd_file[["Brand" , "ASIN" , 'Amazon.ca SalesRank']]

    pd_sorted = pd_work.sort_values(by =["Brand" , "Amazon.ca SalesRank"])
    result = pd_sorted["Brand"].value_counts()


    liste = []
    for k , v in result.items():
        if v >= 3:
            liste.append(k)

    dataframe = pd.DataFrame()
    for _ in range(len(liste)):    
        df =pd_sorted.groupby("Brand").get_group(liste[_]).tail(-2)
                
        dataframe = dataframe.append(df ,ignore_index=True)    


    dataframe.to_excel("excel.xlsx" , "ASIN" , encoding="UTF-8")

    messagebox.showinfo(title= "BİLGİ", message="Dosyanız 'excel.xlsx' ismiyle \n uygulamanın bulundugu klasöre yüklenmiştir ")

def cagir3():
    a = fd.askopenfilename()
    pd_file =pd.read_excel(a)
    
    pd_file['Brand'] = pd_file['Brand'].astype(str)
    pd_work = pd_file[["Brand" , "ASIN" , 'Amazon.ca SalesRank']]

    pd_sorted = pd_work.sort_values(by =["Brand" , "Amazon.ca SalesRank"])
    result = pd_sorted["Brand"].value_counts()


    liste = []
    for k , v in result.items():
        if v >= 4:
            liste.append(k)

    dataframe = pd.DataFrame()
    for _ in range(len(liste)):    
        df =pd_sorted.groupby("Brand").get_group(liste[_]).tail(-3)
                
        dataframe = dataframe.append(df ,ignore_index=True)    


    dataframe.to_excel("excel.xlsx" , "ASIN" , encoding="UTF-8")

    messagebox.showinfo(title= "BİLGİ", message="Dosyanız 'excel.xlsx' ismiyle \n uygulamanın bulundugu klasöre yüklenmiştir ")

def cagir4():
    a = fd.askopenfilename()
    pd_file =pd.read_excel(a)
    
    pd_file['Brand'] = pd_file['Brand'].astype(str)
    pd_work = pd_file[["Brand" , "ASIN" , 'Amazon.ca SalesRank']]

    pd_sorted = pd_work.sort_values(by =["Brand" , "Amazon.ca SalesRank"])
    result = pd_sorted["Brand"].value_counts()


    liste = []
    for k , v in result.items():
        if v >= 5:
            liste.append(k)

    dataframe = pd.DataFrame()
    for _ in range(len(liste)):    
        df =pd_sorted.groupby("Brand").get_group(liste[_]).tail(-4)
                
        dataframe = dataframe.append(df ,ignore_index=True)    


    dataframe.to_excel("excel.xlsx" , "ASIN" , encoding="UTF-8")

    messagebox.showinfo(title= "BİLGİ", message="Dosyanız 'excel.xlsx' ismiyle \n uygulamanın bulundugu klasöre yüklenmiştir ")




def buton2():
    buton2 = Button(frame_genel , text = "Dosya Seciniz" ,font= "Verdana 15 bold", command= cagir2)
    buton2.place(relx = 0.5 , rely = 0.62 , relwidth=0.32)

def buton3():
    
    buton3 = Button(frame_genel , text = "Dosya Seciniz" ,font= "Verdana 15 bold" , command= cagir3)
    buton3.place(relx = 0.5 , rely = 0.62 , relwidth=0.32)

def buton4():

    buton4 = Button(frame_genel , text = "Dosya Seciniz" ,font= "Verdana 15 bold", command= cagir4)
    buton4.place(relx = 0.5 , rely = 0.62 , relwidth=0.32)

var = IntVar()
R1 = Radiobutton(frame_genel, text="2 Adet", variable=var, value=2 , command=buton2)
R1.place(relx=  0.5 , rely = 0.5 , relheight= 0.1 , relwidth= 0.1) 
R2 = Radiobutton(frame_genel, text="3 Adet", variable=var, value=3 , command= buton3)
R2.place(relx=  0.61 , rely = 0.5 , relheight=0.1 , relwidth= 0.1) 
R3 = Radiobutton(frame_genel, text="4 Adet", variable=var, value=4 , command = buton4)
R3.place(relx=  0.72 , rely = 0.5 , relheight=0.1 , relwidth= 0.1) 



master.mainloop()