# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 20:29:00 2021

@author: bezbakri
"""

import calendar
from tkinter import *
from datetime import datetime
import sys
sys.path.append('C:/MyFolder/school_trash/class12/comp/practicals/PyCal2/')
import src.db as db


db.initialise()
import sqlite3



def add_event():
    addition = Tk()
    addition.title("Add events")
    addition.configure(background = "#B1F5F5")
    addition.geometry("800x800")
    
    addition.mainloop()