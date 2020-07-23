from tkinter import *
root=Tk()
c=Canvas(root,height=600,width=800)
c.pack()
p=PhotoImage(file='daldo.gif')
f=c.create_image(0,0,anchor=NW,image=p)

root.mainloop()
