import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

root = Tk()
root.title("Text convert to Speech")
root.geometry("900x500+200+200")
root.resizable(False, False)
root.configure(bg="#430b66")

#icon of app
icon = PhotoImage(file="speak.png")
root.iconphoto(False, icon)

#top of the frame
top_frame = Frame(root, bg="white", width=900, height=100)
top_frame.place(x=0, y=0)
logo = PhotoImage(file="speaker logo.png")
Label(top_frame, image=logo, bg="white").place(x=10, y=5)
Label(top_frame, text="TEXT CONVERT TO SPEECH", font="arial 20 bold", bg="white", fg="#ab7fc7").place(x=100, y=30)

#text input area
text_input_area = Text(root, font="Robote 20", bg="#ab7fc7", relief=GROOVE, wrap=WORD)
text_input_area.place(x=10, y=150, width=500, height=300)

Label(root, text="VOICE", font="arial 15 bold", bg="#430b66", fg="white").place(x=580, y=160)
Label(root, text="SPEED", font="arial 15 bold", bg="#430b66", fg="white").place(x=760, y=160)

gender_combobox = Combobox(root, values=['Male', 'Female'], font="arial 14", state='r', width=10)
gender_combobox.place(x=550, y=200)
gender_combobox.set('Female')

speed_combobox = Combobox(root, values=['Normal', 'Fast', 'Slow'], font="arial 14", state='r', width=10)
speed_combobox.place(x=730, y=200)
speed_combobox.set('Normal')

root.mainloop()