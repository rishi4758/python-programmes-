from tkinter import *
b=Tk()
def fun():
 a=int(input("enter first number"))
 o=int(input("enter second number"))
 d=a+o
 print(d)
l1=Label(b,text='nomashkar')
l1.grid(column=50,row=5)
b.geometry("400x400")
a1=Button(b,text="submit",command=fun)
a1.grid()

b.mainloop()
