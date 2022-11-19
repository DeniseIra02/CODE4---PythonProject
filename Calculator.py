from tkinter import *

root = Tk()
root.title("Addition Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def buttonclick(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0,str(current) + str(number))

button1 = Button(root, text="1", padx=40, pady=20, command=lambda: buttonclick(1))
button2 = Button(root, text="2", padx=40, pady=20, command=lambda: buttonclick(2))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: buttonclick(3))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda: buttonclick(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: buttonclick(5))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda: buttonclick(6))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda: buttonclick(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: buttonclick(8))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: buttonclick(9))
button0 = Button(root, text="0", padx=40, pady=20, command=lambda: buttonclick(0))
buttonadd = Button(root, text="+", padx=40, pady=20, command=lambda: buttonclick())
buttonequal = Button(root, text="=", padx=40, pady=20, command=lambda: buttonclick())
buttonclear = Button(root, text="Clear", padx=40, pady=20, command= buttonclick)

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)
buttonclear.grid(row=4, column=1)

buttonadd.grid(row=5, column=0)
buttonequal.grid(row=5, column=1)

root.mainloop()