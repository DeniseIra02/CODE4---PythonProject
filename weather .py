import tkinter as tk
import requests
import time 

def get_theWeather():
    city = textfield.get()

canvas = tk.Tk()
canvas.geometry ("600x500")
canvas.title("Weather Forecast App")

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textfield = tk.Entry(canvas, font = t)
textfield.pack(pady=20)
textfield.focus()

label1 = tk.Label(canvas, font = t)
label1.pack()
label2 = tk.Label(canvas, font = f)
label2.pack()

canvas.mainloop()