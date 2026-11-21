from tkinter import *

window=Tk()
window.title('Login App')
window.geometry("400x400")

frame=Frame(master=window,height=200,width=360,bg='#d2d7da')
lb1=Label(frame,text="Full Name",bg='#3895D3',fg='white',width=12)
lb2=Label(frame,text="Email Id",bg='#3895D3',fg='white',width=12)
lb3=Label(frame,text="Enter Password",bg='#3895D3',fg='white',width=12)

name_entry=Entry(frame)
email_entry=Entry(frame)
password_entry=Entry(frame,show="*")

def display():
    name=name_entry.get()
    greet="Hey " + name
    message=n\