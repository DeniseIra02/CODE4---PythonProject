import tkinter as ui 

root_window = ui.Tk()

digital_clock = ui.Label(root_window, text="00:00:00", font="Helvetica 72 bold")
digital_clock.pack()

root_window.mainloop()