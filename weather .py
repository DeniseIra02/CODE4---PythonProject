import tkinter as tk
import requests
import time 

canvas = tk.Tk()
canvas.geometry ("600x500")
canvas.title("Weather Forecast App")

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textfield = tk.Entry(canvas, font= t)
textfield.pack(pady=20)
textfield.focus()

