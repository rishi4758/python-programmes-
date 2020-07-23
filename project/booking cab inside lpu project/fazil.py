from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import webbrowser
class pro:
    win=Tk()

    canvas=Canvas(win,height=849,width=1235)
    canvas.pack()

    ######### login page definition
    def login(self):
        pro.canvas.delete("all")


        pict = PhotoImage(file='ola.gif')  # importing image as backfground
        pro.canvas.create_image(0,0,anchor=NW,image=pict)


        ba = Button(pro.canvas, text="SIGN IN",command=self.dashboard)
        pro.canvas.create_window(500,250, window=ba)




        ba = Button(pro.canvas, text="REGISTER", command=self.registration)
        pro.canvas.create_window(600,250, window=ba)

        lbu = Label(pro.canvas, text="USERNAME")
        pro.canvas.create_window(400,100,window=lbu)


        bp = Label(pro.canvas, text="PASSWORD")
        pro.canvas.create_window(400,180,window=bp)


        eu = Entry(pro.canvas)
        pro.canvas.create_window(550, 100,window=eu)

        ep = Entry(pro.canvas, show="*")
        pro.canvas.create_window(550, 180,window=ep)


        ##### creating a button of available routes

        web=Button(pro.canvas,text="AVAILABLE ROUTES",command=self.routes)
        pro.canvas.create_window(400,250,window=web)








        pro.win.mainloop()
     ############# this is the function of routes avialable in lpu
    def routes(self):
        webbrowser.open(url="https://www.google.com/maps/place/Lovely+Professional+University/@31.2602396,75.7073591,18.38z/data=!4m5!3m4!1s0x391a5a594d22b88d:0x4cc934c58d0992ec!8m2!3d31.253603!4d75.703669")



    ################# this is the actual workking definition
    def dashboard(self):
        pro.canvas.delete("all")

        self.dash=PhotoImage(file="dash.png")
        pro.canvas.create_image(80,0,image=self.dash,anchor=NW)
        la=Label(pro.canvas,text="LETS RIDE IN LPU",font="times 40 underline",fg="RED")
        pro.canvas.create_window(400,20,window=la)

        mlabel=Label(pro.canvas,text='MOBILE NO:',font="20",fg="GREEN")
        pro.canvas.create_window(300,200,window=mlabel)

        mentry=Entry(pro.canvas)
        pro.canvas.create_window(450,200,window=mentry)

        ########## places

        fromtuple=("main gate","block 1","block 2","block 3","block 4","block 5","block 6",
                   "block 7", "block 8", "block 9", "block 14", "block 26", "block 27",
                   "block 28", "block 29", "block 30", "block 31", "block 32",
                   "block 33", "block 34", "block 35", "block 36", "block 37",
                   "block 38",

                   "GH-9","GH-10","GH-11","GH-12","GH-13"
                   ,"GH-15","GH-16","GH-17","GH-18","GH-19","GH-20",
                   "BH-1","BH-2","BH-3","BH-4","BH-5",
                   "BH-6", "BH-7", "BH-8", "BH-9", "BH-10",
                   "block 54", "block 55", "block 56", "block 57", "block 58",



                   )


        fro=Label(pro.canvas,text="FROM:",fg="green",font="20")
        pro.canvas.create_window(280,250,window=fro)






        totuple=("main gate","block 1","block 2","block 3","block 4","block 5","block 6",
                   "block 7", "block 8", "block 9", "block 14", "block 26", "block 27",
                   "block 28", "block 29", "block 30", "block 31", "block 32",
                   "block 33", "block 34", "block 35", "block 36", "block 37",
                   "block 38",

                   "GH-9","GH-10","GH-11","GH-12","GH-13"
                   ,"GH-15","GH-16","GH-17","GH-18","GH-19","GH-20",
                   "BH-1","BH-2","BH-3","BH-4","BH-5",
                   "BH-6", "BH-7", "BH-8", "BH-9", "BH-10",
                   "block 54", "block 55", "block 56", "block 57", "block 58",



                   )


        to=Label(pro.canvas,text="TO:",fg="green",font="20")
        pro.canvas.create_window(270,300,window=to)


        como2=ttk.Combobox(width=60)
        como2['values']=fromtuple
        pro.canvas.create_window(500,300,window=como2)

        fare = Label(pro.canvas, text="RS:", fg="green", font="20")
        pro.canvas.create_window(270, 350, window=fare)

        entry=Entry(pro.canvas)
        pro.canvas.create_window(370,350,window=entry)

        day=Label(pro.canvas, text="Day:", fg="green", font="20")


        daytuple=("SUNDAY","MONDAY","TUESDAY","THURSDAY","FRIDAY","SATURDAY")


        daycombo=ttk.Combobox(width=60)
        daycombo['values']=daytuple
        pro.canvas.create_window(500,250,window=daycombo)
























############ thi is the registration page
    def registration(self):
        pro.canvas.delete("all")

        #self.pict2 = PhotoImage(file='fazil.gif')  # importing image as backfground
        #pro.canvas.create_image(0,0,anchor=NW,image=self.pict2)


        T = Label(pro.canvas,text="SIGN UP TO RIDE", width=100, bg='#06FCFC', fg="black", font="20")
        pro.canvas.create_window(0,0,window=T,anchor=NW)

        ba = Button(pro.canvas, text="Homepage", command=self.login)
        pro.canvas.create_window(38,12, window=ba)


        #### adding the information
        name = Label(pro.canvas, text="NAME")
        pro.canvas.create_window(185, 100, window=name)

        name_entry = Entry(pro.canvas)
        pro.canvas.create_window(230,140,window=name_entry)

        username = Label(pro.canvas, text="User Name")
        pro.canvas.create_window(470, 100, window=username)

        user_entry = Entry(pro.canvas)
        pro.canvas.create_window(500, 140, window=user_entry)




        regid = Label(pro.canvas, text="REGISTRATION ID")
        pro.canvas.create_window(210, 190, window=regid)



        regid_ent = Entry(pro.canvas, width=65)
        pro.canvas.create_window(360, 230, window=regid_ent)




        phone = Label(pro.canvas, text="PHONE NUMBER")
        pro.canvas.create_window(210, 280, window=phone)

        phone_entry = Entry(pro.canvas, width=65)
        pro.canvas.create_window(360,320, window=phone_entry)

        email = Label(pro.canvas, text="EMAIL_ID")
        pro.canvas.create_window(190,370, window = email)



        email_ent = Entry(pro.canvas, width=65)
        pro.canvas.create_window(360, 410, window=email_ent)

        passw = Label(pro.canvas, text="CREATE PASSWORD")
        pro.canvas.create_window(210, 460, window=passw)


        passw_entry = Entry(pro.canvas, width=65)
        pro.canvas.create_window(360,500, window=passw_entry)




        c=Button(pro.canvas, text="SUBMIT",command=self.valid, background="#06FCFC", fg="black", activebackground="red",cursor="hand1")
        pro.canvas.create_window(400,600, window=c)

    def valid(self):
        messagebox.showinfo("FORM SUBMISSION","CONGRATS YOU ARE  THE  NEW MEMBER")









s=pro()
s.login()
