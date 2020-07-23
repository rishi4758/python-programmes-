from tkinter import *
from tkinter import messagebox
win=Tk()
canvas=Canvas(win,height=650,width=800)
canvas.pack()

def valid():
    password = passw_entry.get()
    flag = 0
    while True:
        if (len(password)<8): 
            flag = -1
            break
        elif not re.search("[a-z]", password): 
            flag = -1
            break
        elif not re.search("[A-Z]", password): 
            flag = -1
            break
        elif not re.search("[0-9]", password): 
            flag = -1
            break
        elif not re.search("[_@$]", password): 
            flag = -1
            break
        elif re.search("\s", password): 
            flag = -1
            break
        else: 
            flag = 0
            print("Valid Password")
            save()
            messagebox.showinfo("FORM SUBMISSION","CONGRATS YOU ARE  THE  NEW MEMBER")
            break
  
    if flag ==-1:
         print("Not a Valid Password")       
         messagebox.showinfo("FORM SUBMISSION","Not valid Password")

def save():
 n=name_entry.get()
 u=user_entry.get()
 r=regid_ent.get()
 p=phone_entry.get()
 e=email_ent.get()
 pw=passw_entry.get()
 input=open("data.txt","w")
 input.write("\n")
 input.write("\n")
 input.write("User")
 input.write("\n")
 input.write(n)
 input.write("\n")
 input.write(u)
 input.write("\n")
 input.write(r)
 input.write("\n")
 input.write(p)
 input.write("\n")
 input.write(e)
 input.write("\n")
 input.write(pw)
 input.close()

 input=open("user.txt","w")
 input.write("\n")
 input.write("\n")
 input.write("User")
 input.write("\n")
 input.write(u)
 input.write("\n")
 input.write(pw)

name = Label(canvas, text="NAME")
canvas.create_window(185, 100, window=name)

name_entry = Entry(canvas)
canvas.create_window(230,140,window=name_entry)

username = Label(canvas, text="User Name")
canvas.create_window(470, 100, window=username)

user_entry = Entry(canvas)
canvas.create_window(500, 140, window=user_entry)




regid = Label(canvas, text="REGISTRATION ID")
canvas.create_window(210, 190, window=regid)



regid_ent = Entry(canvas, width=65)
canvas.create_window(360, 230, window=regid_ent)




phone = Label(canvas, text="PHONE NUMBER")
canvas.create_window(210, 280, window=phone)

phone_entry = Entry(canvas, width=65)
canvas.create_window(360,320, window=phone_entry)

email = Label(canvas, text="EMAIL_ID")
canvas.create_window(190,370, window = email)



email_ent = Entry(canvas, width=65)
canvas.create_window(360, 410, window=email_ent)

passw = Label(canvas, text="CREATE PASSWORD")
canvas.create_window(210, 460, window=passw)


passw_entry = Entry(canvas, width=65)
canvas.create_window(360,500, window=passw_entry)


c=Button(canvas, text="SUBMIT",command=valid, background="#06FCFC", fg="black", activebackground="red",cursor="hand1")
canvas.create_window(400,600, window=c)



    
win.mainloop()
