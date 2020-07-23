from tkinter import *
b=Tk()
def fun():
 a=int(input("enter first number"))
 o=int(input("enter second number"))
 d=a+o
 print(d)
l1=Label(b,text='nomashkar' ,bg="red",fg="BLUE")
l1.grid(column=4)
b.geometry("400x400")



b.mainloop()
