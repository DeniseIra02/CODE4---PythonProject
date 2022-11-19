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
top_frame = Frame(root, bg="white", width=900, height=80)
top_frame.place(x=0, y=0)
Label(top_frame, text="TEXT CONVERT TO SPEECH", font="arial 20 bold", bg="white", fg="#ab7fc7").place(x=50, y=30)

#text input area
text_input_area = Text(root, font="Robote 20", bg="#ab7fc7", relief=GROOVE, wrap=WORD)
text_input_area.place(x=10, y=150, width=500, height=300)

root.mainloop()