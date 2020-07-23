from tkinter import *


w1=Tk()
ok=Button(w1,text='ok',command=ok)
cancel=Button(w1,text='Cancel')
cancel.pack()
ok.pack()

uber=PhotoImage(file="homepic.gif")
img=PhotoImage(file="registerpage.gif")



canvas=Canvas(w1)
canvas.create_image(100,100,image=uber)

canvas.pack()
w1.mainloop()
