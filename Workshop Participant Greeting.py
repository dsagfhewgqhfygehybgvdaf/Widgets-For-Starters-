from tkinter import *
from datetime import date
window=Tk()
window.title("Workshop Participant Greeting")
window.geometry("500x500")
lb1=Label(text='Hello!',fg='white',bg="#3895D3",height=1,width=300)
lb1_nametext=Label(text='Enter Name:',bg="#3895D3")
lb1_nameentry=Entry()
def display():
    name=lb1_nameentry.get()
    text_box.delete(1.0,END)
    greeting="Hello" + name + "!\n"
    message="Welcome to the Workshop!\n"
    workshop_time="Date: " + str(date.today())
    text_box.insert(END, greeting)
    text_box.insert(END, message)
    text_box.insert(END, workshop_time)
text_box=Text(height=4,width=40)
welcome_button= Button(text="Check in",command=display,height=1,bg="#1261A0",fg="white")
lb1.pack()
lb1_nametext.pack(pady=10)
lb1_nameentry.pack()
welcome_button.pack(pady=10)
text_box.pack()
window.mainloop()
