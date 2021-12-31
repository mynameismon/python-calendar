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
event_to_add = ""






def getValue():
    global event_to_add
    event_to_add = userInput.get()
    
    event_var.set("")



def add_event():
    addition = Tk()
    addition.title("Add events")
    addition.configure(background = "#B1F5F5")
    addition.geometry("800x800")
    event_var = StringVar()
    header = Label(addition, text = "Add an event. Type it in YYYY/MM/DD HH:mm:SS Format", font = "consolas 11")
    header.grid(row = 2, column = 1, padx = 20)
    
    userInput = Entry(addition, textvariable = event_var).grid(row = 4, column = 1)
    
    buttonAddEvent = Button(addition, text = "Add event", command = "call_result").grid(row = 6, column = 1)
    
    
    
    
    
    addition.mainloop()