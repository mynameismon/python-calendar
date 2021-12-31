# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 16:34:45 2021

@author: bezbakri
"""

import calendar
from tkinter import *
from datetime import datetime
import src.db as db


db.initialise()
import sqlite3



def show_event():
    display_event = Tk()
    display_event.title("Show events")
    display_event.configure(background = "#B1F5F5")
    display_event.geometry("800x800")
    header = Label(display_event, text = "List of events", font = "consolas 11")
    header.grid(row = 2, column = 1, padx = 20)
    
    
    
    #where the events are shown
    listbox = Listbox(display_event).grid(row = 4, column = 1)
    
    
    #dump them in a list and do something like this
    #for i in list of events:
        #listbox.insert(index_starting_from_1, i)
    
    
    
    
    
    display_event.mainloop()