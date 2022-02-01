

from tkinter import *

import calendar_display 
import add_events
import show_events
import src.db as db

db.initialise()





main = Tk()
main.title("Calendar")
main.configure(background = "#B1F5F5")
main.geometry("500x500")
Label(main, text = "What do you want to see?", font = "Helvetica 12").grid(row = 1, column = 2)
Button(main, text = "View Calendar", command = calendar_display.DisplayCalendar).grid(row = 3, column = 0)
Button(main, text = "Add events", command = add_events.add_event).grid(row = 3, column = 1)
Button(main, text = "Show events", command = show_events.show_event).grid(row = 3, column = 2)




main.mainloop()
