from tkinter import *
root=Tk()
a=Entry(root,width=20,relief="raised",bd=5,bg="white",fg="white",cursor="man",highlightcolor="red")
a.insert(0,'enter name')
a.config(fg = 'grey',font='Times 15')
a.grid(row=1,column=1)
b1=Button(text="+",activebackground="royalblue",activeforeground="white",bd=5,fg="white",bg="cornsilk4",font="halvetica 20",highlightcolor="deeppink3")
b1.grid(row=4,column=3)
root.mainloop()
