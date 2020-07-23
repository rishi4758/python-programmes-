from tkinter import *
b=Tk()
def fun1():
    val=entry.get()
    val1=entry.get()
    sum=val+val1
    sum.insert()
def fun2():
    val=entry.get()
    val1=entry.get()
    sum=val-val1
    sum.insert()
def fun3():
    val=entry.get()
    val1=entry.get()
    sum=val*val1
    sum.insert()
def fun4():
    val=entry.get()
    val1=entry.get()
    sum=val/val1
    sum.insert()
def fun5():
    val=entry.get()
    val1=entry.get()
    sum=val**val1
    sum.insert()
l1=Label(b,text="input 1")
l2=Label(b,text="input 2")
l3=Label(b,text="operation")
l4=Label(b,text="output")
b1=Button(b,text="+",command=fun1)
b2=Button(b,text="-",command=fun2)
b3=Button(b,text="*",command=fun3)
b4=Button(b,text="/",command=fun4)
b5=Button(b,text="**",command=fun5)
l1.place(x=200,y=100)
l2.place(x=400,y=100)
l3.place(x=600,y=100)
l4.place(x=800,y=100)
x=Entry()
y=Entry()
z=Entry()
u=Entry()
x.place(x=200,y=300)
y.place(x=400,y=300)
z.place(x=600,y=300)
u.place(x=800,y=300)
