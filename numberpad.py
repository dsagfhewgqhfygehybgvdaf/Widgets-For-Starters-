from tkinter import *
window=Tk()
window.title('Number pad')
window.geometry('250x300')

no=[[1,2,3],[4,5,6],[7,8,9], ['*',0,'#']]

for i in range(4):
    window.columnconfigure(i,weight=1,minsize=75)
    window.rowconfigure(i,weight=1,minsize=50)
    for j in range(0,3):
        frame=Frame(master = window,relief=RAISED,borderwidth=1)
        frame.grid(row=i,column=j)
        lb1=Label(master=frame,text=no[i][j],bg='#d0efff')
        lb1.pack(padx=3, pady=3)
window.mainloop()
                  
