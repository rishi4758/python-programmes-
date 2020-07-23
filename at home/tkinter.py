from tkinter import *;
tk=Tk();
# widget like button,label, textboxes input graphics will be enter inside this body
#there are 15 types of widgets(tags in html) in python and each widget have there attributes
#like font-size,button tag etc
def fun1():
    print("button is ruunning");
s=Button(tk,text="hello", bg="red", activebackground="blue", height="10",width="10", command=fun1).grid(row=0,column=0,padx=30);
s1=Canvas(tk,bg="green",height="40",width="400").grid(row=1,column=0,pady=20);
# inside canvas we can place aarc image and can draw anything cavas object.widgetname ex:s1.arc()


b1=Label(tk,text="name",).grid(row=3,column=0,sticky=W);
b2=Entry(tk).place(x=100,y=230);

tk.mainloop();
