import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

root = Tk()
root.title("Text convert to Speech")
root.geometry("900x500")
root.resizable(False, False)
root.configure(bg="#430b66")

#icon of app
icon = PhotoImage(file="speak.png")
root.iconphoto(False, icon)

root.mainloop()