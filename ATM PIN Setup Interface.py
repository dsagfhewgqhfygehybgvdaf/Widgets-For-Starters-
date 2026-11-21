from tkinter import *

window=Tk()
window.title("ATM PIN Setup Interface")
window.geometry("400x500")

details_frame= Frame(
    master=window,
    height=150,
    width=360,
    bg="#d0efff"
)

name_label=Label(
    details_frame,
    text="Account Name",
    bg="#3895D3",
    fg="white",
    width=14
)

pin_label=Label(
    details_frame,
    text="Create PIN",
    bg="#3895D3",
    fg="white",
    width=14
)

name_entry= Entry(details_frame)

pin_entry= Entry(details_frame, show="*")

def confirm_pin():
    acount_name=name_entry.get()
    pin=pin_entry.get

    message_box.delete(1.0, END)

    if account_name=="" or pin =="":
        message_box.insert(
            END,
            "Please enter the account name and PIN"
        )
    else:
        message=(
            "Hello " + account_name +
            "\nYour ATM PIN has been set succesfully"
        )