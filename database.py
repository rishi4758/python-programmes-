import sqlite3
from tkinter import *
from tkinter import messagebox
c=sqlite3.connect("trs2h1e.db")
s=c.cursor()
def fun1():
  s.execute("create table emp5(name Text,mobile Text,age Text,pincode Text,password text)")
  s.execute("insert into emp5 values('jzk','lks','jkzns','kjzas','azkj')")
  s.execute("insert into emp5 values(?,?,?,?,?)",(a1.get(),a2.get(),a3.get(),a4.get(),a5.get()))
  t=a5.get()
  x=len(t)
  u=0
  y=0
  for i in t:
    if i.isupper():
      u=1
    elif i.islower():
      y=1
  if u==1 or y==1:
      messagebox.showinfo("warning","password should be in digits")
  print(x)
  f=s.execute("select * from emp5")
  print(f.fetchall())
  b.destroy()
  
b=Tk()
c1=Label(b,text="Name").grid(row=0,column=0)
c2=Label(b,text="mobile").grid(row=1,column=0)
c3=Label(b,text="age").grid(row=2,column=0)
c4=Label(b,text="pincode").grid(row=3,column=0)
c5=Label(b,text="password").grid(row=4,column=0)
b1=Button(b,text="submit",command=fun1).grid(row=5,column=1)
a1=Entry(b)
a2=Entry(b)
a3=Entry(b)
a4=Entry(b)
a5=Entry(b)
a1.grid(row=0,column=1)
a2.grid(row=1,column=1)
a3.grid(row=2,column=1)
a4.grid(row=3,column=1)
a5.grid(row=4,column=1)
b1=Button(b,text="submit",command=fun1).grid(row=5,column=1)

b.mainloop()
