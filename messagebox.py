from tkinter import *
from tkinter import messagebox

window=Tk()
window.geometry("200x200")

def msg():
    messagebox.askyesno("Confirm?","Do you want to continue?")

button=Button(window, text="Scan for Virus", command=msg)
button.place(x=40, y=80)

window.mainloop()