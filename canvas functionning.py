from tkinter import *
from tkinter import ttk
root=Tk()
c=Canvas(root,width=500,height=500)
c.pack()

c.create_line(0,50,50,50,fill="red")
t=("2","3")
x=ttk.Combobox(width=50)
x['values']=t
c.create_window(2,10,window=x)
root.mainloop()
