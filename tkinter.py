# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 21:22:07 2021

@author: bezbakri
"""

import calendar
from tkinter import *
from datetime import datetime

current_date = datetime.now()
year = int(current_date.strftime("%Y"))

def PrevYear():
    global window
    window.destroy()
    global year
    year -=1
    window = Tk()
    window.title("Calendar")
    window.configure(background = "#B1F5F5")
    window.geometry("800x800")
    output = Label(window, text = calendar.calendar(year), font = "Consolas 11")
    output.grid(row = 5, column = 1, padx = 20)
    Button(window, text = "Last Year", command = PrevYear).grid(row = 7, column = 0)
    Button(window, text = "Next Year", command = NextYear).grid(row = 7, column = 2)
    window.mainloop()


def NextYear():
    global window
    window.destroy()
    global year
    year +=1
    window = Tk()
    window.title("Calendar")
    window.configure(background = "#B1F5F5")
    window.geometry("800x800")
    output = Label(window, text = calendar.calendar(year), font = "Consolas 11")
    output.grid(row = 5, column = 1, padx = 20)
    Button(window, text = "Last Year", command = PrevYear).grid(row = 7, column = 0)
    Button(window, text = "Next Year", command = NextYear).grid(row = 7, column = 2)
    window.mainloop()



window = Tk()
window.title("Calendar")
window.configure(background = "#B1F5F5")
window.geometry("800x800")
output = Label(window, text = calendar.calendar(year), font = "Consolas 11")
output.grid(row = 5, column = 1, padx = 20)
Button(window, text = "Last Year", command = PrevYear).grid(row = 7, column = 0)
Button(window, text = "Next Year", command = NextYear).grid(row = 7, column = 2)



window.mainloop()