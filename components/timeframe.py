import tkinter as tk

# Borrowed from: https://stackoverflow.com/a/59326732/9496502
class TimeFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.hourstr=tk.StringVar(self,'10')
        self.hour = tk.Spinbox(self,from_=0,to=23,wrap=True,textvariable=self.hourstr,width=2,state="readonly")
        self.minstr=tk.StringVar(self,'59')

        self.min = tk.Spinbox(self,from_=0,to=59,wrap=True,textvariable=self.minstr,width=2)    # ,state="readonly"
        self.secstr=tk.StringVar(self,'00')
        self.sec = tk.Spinbox(self,from_=0,to=59,wrap=True,textvariable=self.secstr,width=2) 

        self.last_valueSec = ""
        self.last_value = ""        
        self.minstr.trace_add("write",self.trace_var)
        self.secstr.trace_add("write",self.trace_varsec)

        self.hour.grid()
        self.min.grid(row=0,column=1)
        self.sec.grid(row=0,column=2)

    def trace_var(self,*args):
        if self.last_value == "59" and self.minstr.get() == "0":
            self.hourstr.set(int(self.hourstr.get())+1 if self.hourstr.get() != "23" else 0)  
        elif self.last_value == "0" and self.minstr.get() == "59":
            self.hourstr.set(int(self.hourstr.get()) - 1 if self.hourstr.get() != "00" else "23")   
        self.last_value = self.minstr.get()

    def trace_varsec(self,*args):
        if self.last_valueSec == "59" and self.secstr.get() == "0":
            self.minstr.set(int(self.minstr.get())+1 if self.minstr.get() !="59" else 0)
            self.trace_var() 
        elif self.last_valueSec == "0" and self.secstr.get() == "59":
            self.minstr.set(int(self.minstr.get()) - 1 if self.minstr.get() != "00" else "59")
            self.trace_var()       
        self.last_valueSec = self.secstr.get()
