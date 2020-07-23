from tkinter import *
from tkinter import messagebox
win=Tk()
canvas=Canvas(win,height=650,width=800)
canvas.pack()

def validation():
    f=open("user.txt","r")
    a=f.readlines()
    b,c=0,0
    for i in a:
        if i==eu.get():
            b=1
    for i in a:
        if i==ep.get():
            c=1
    if b!=1 and c!=1:
        messagebox.showinfo("Invalid","Invalid Username or Password")
    


lbu = Label(canvas, text="USERNAME")
canvas.create_window(400,100,window=lbu)


bp = Label(canvas, text="PASSWORD")
canvas.create_window(400,180,window=bp)


eu = Entry(canvas)
canvas.create_window(550, 100,window=eu)

ep = Entry(canvas, show="*")
canvas.create_window(550, 180,window=ep)

ba = Button(canvas, text="SIGN IN",command=validation)
canvas.create_window(500,250, window=ba)

win.mainloop()
