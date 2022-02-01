# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 20:29:00 2021

@author: bezbakri
"""

import calendar
from tkinter import *
from datetime import datetime
import src.db as db


db.initialise()
import sqlite3





#the input variable name
event_to_add_date = ""
event_to_add_name = ""






def getValue():
    global event_to_add
    event_to_add_date = userInput_date.get()
    event_to_add_name = userInput_name.get()
    event_var_date.set("")
    event_var_name.set("")



def add_event():
    addition = Tk()
    addition.title("Add events")
    addition.configure(background = "#B1F5F5")
    addition.geometry("800x800")
    event_var_date = StringVar()
    event_var_name = StringVar()
    header = Label(addition, text = "Add an event. Type it in YYYY/MM/DD HH:mm:SS Format", font = "consolas 11")
    header.grid(row = 2, column = 1, padx = 20)
    
    userInput_date = Entry(addition, textvariable = event_var_date).grid(row = 4, column = 1)
    header = Label(addition, text = "Type in the event name", font = "consolas 11")
    header.grid(row = 6, column = 1, padx = 20)
    userInput_name = Entry(addition, textvariable = event_var_name).grid(row = 7, column = 1)

    buttonAddEvent = Button(addition, text = "Add event", command = "call_result").grid(row = 9, column = 1)
    
    
    
    
    
    addition.mainloop()