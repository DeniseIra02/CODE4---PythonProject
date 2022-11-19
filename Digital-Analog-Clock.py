import tkinter as ui 
import time

root_window = ui.Tk()

def current_clock():
    hours = time.strftime("%I")
    minutes = time.strftime("%M")
    seconds = time.strftime("%S")
    am_pm = time.strftime("%p ")
    
    timetext= hours + ":" + minutes + ":" + seconds + ":" + " " + am_pm
    digital_clock.config(text=timetext)

digital_clock = ui.Label(root_window, text="00:00:00", font="Helvetica 72 bold")
digital_clock.pack()

root_window.mainloop()