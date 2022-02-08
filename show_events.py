# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 16:34:45 2021

@author: bezbakri
"""

import calendar
from datetime import datetime
from components.tableview import MultiColumnListbox
import src.api as api


try:
    import Tkinter as tk
    import tkFont
    import ttk
except ImportError:  # Python 3
    import tkinter as tk
    import tkinter.font as tkFont
    import tkinter.ttk as ttk



def show_event():
    display_event = tk.Tk()
    display_event.title("Show events")
    display_event.configure(background = "#B1F5F5")
    display_event.geometry("800x800")
    header = tk.Label(display_event, text = "List of events", font = "consolas 11")
    header.grid(row = 2, column = 1, padx = 20)
    
    
    events = api.get_events()
    event_headers = ["Title", "Start Time", "End Time", "Timezone"]
    print(events)
    #where the events are shown
    listbox = MultiColumnListbox(display_event, event_headers, events)
    # listbox.grid(row = 4, column = 1)

       
    
    display_event.mainloop()