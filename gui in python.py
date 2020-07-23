from tkinter import *
win=Tk()
def fun1():
    print("u are logging out")
def cb():
    print("variable is")
l1=Label(win,text="hi i am cool",bg='red',fg='blue').grid(row=0,column=1)
b1=Button(win,text="submit",command=fun1,anchor="center").grid(row=1,column=1)
Button(win, font=('courier',10), text='CE',width=4,height=2, command=lambda: click('CE')).grid(row=0,column=4)
Button(win, font=('courier',10), text='C',width=4,height=2, command=lambda: click('C')).grid(row=0,column=5)
Button(win, font=('courier',10), text='7',width=4,height=2, command=lambda: click('7')).grid(row=1,column=1)
Button(win, font=('courier',10), text='8',width=4,height=2, command=lambda: click('8')).grid(row=1,column=2)
Button(win, font=('courier',10), text='9',width=4,height=2, command=lambda: click('9')).grid(row=1,column=3)
Button(win, font=('courier',10), text='4',width=4,height=2, command=lambda: click('4')).grid(row=2,column=1)
Button(win, font=('courier',10), text='5',width=4,height=2, command=lambda: click('5')).grid(row=2,column=2)
Button(win, font=('courier',10), text='6',width=4,height=2, command=lambda: click('6')).grid(row=2,column=3)
Button(win, font=('courier',10), text='1',width=4,height=2, command=lambda: click('1')).grid(row=3,column=1)
Button(win, font=('courier',10), text='2',width=4,height=2, command=lambda: click('2')).grid(row=3,column=2)
Button(win, font=('courier',10), text='3',width=4,height=2, command=lambda: click('3')).grid(row=3,column=3)
Button(win, font=('courier',10), text='0',width=4,height=2, command=lambda: click('0')).grid(row=4,column=1)
Button(win, font=('courier',10), text='+/‐',width=4,height=2, command=lambda: click('+/‐')).grid(row=4,column=2)
Button(win, font=('courier',10), text='.',width=4,height=2, command=lambda: click('.')).grid(row=4,column=3)
e1=Entry(win,highlightthickness="10")
e1.grid(row=20,column=1)
e2=Entry(win,highlightcolor='green',highlightthickness="10")
e2.grid(row=21,column=1)
frame = Frame(win)
frame.grid()
c = Checkbutton(
win, text="Enable T").grid(row=23,column=3)
def change():
 print("Station = ") , var.get()
root = Tk()
stations = 'WAAL' , 'WSKG' , 'WSQX' , 'WNBF'
f = Frame(relief=RAISED , borderwidth=5)
var = StringVar()
for station in stations:
  radio = Radiobutton(f, text=station, variable=var ,value=station)
  radio.grid(row=25,column=2)
f.grid(row=26,column=2)
Button(root,text='New' , command=(lambda: change())).pack(pady=10)
var.set('WAAL') #initalize the set of radio buttons

win.mainloop()
