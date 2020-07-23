from tkinter import *

def okk():
    top = Toplevel()
    top.title("Confirmation")
    canvas=Canvas(top)
    canvas.create_image(100,100,image=img)
    canvas.pack()

    back= Button(top, text="Back", command=top.destroy)
    back.pack()
    
def ok():
    top = Toplevel()
    top.title("Confirmation")
    canvas=Canvas(top)
    canvas.create_image(100,100,image=img)
    canvas.pack()

    back= Button(top, text="Back", command=top.destroy)
    back.pack()
    okk()

   

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
