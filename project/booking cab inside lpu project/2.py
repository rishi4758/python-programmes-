.from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import webbrowser
class pro:
    win=Tk()
    first=[0,0]
    second=[0,0]

    canvas=Canvas(win,height=849,width=1235)
    canvas.pack()

    ######### login page definition
    def login(self):
        pro.canvas.delete("all")


        pict = PhotoImage(file='ola.gif')  # importing image as backfground
        pro.canvas.create_image(0,0,anchor=NW,image=pict)

        def validation():
            f=open("user.txt","r")
            a=f.readlines()
            b,c=0,0
            for i in a:
                if i==eu.get():
                    b=1
            for i in a:
                if i==ep.get():
                    c=1
            if b!=1 and c!=1:
                messagebox.showinfo("Invalid","Invalid Username or Password")
            else:
                self.dashboard()        

        ba = Button(pro.canvas, text="SIGN IN",command=validation)
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
    







    def fromm(self,event):
        c = self.forcomo.get()
        pro.first= self.fromdict[c]


#this is first combofunction 


    def toplace(self,event):
        keynew=self.newcomb.get()
        pro.second=self.todict[keynew]



#   combobinding
    def  calculate_fare(self):
        x=(self.second[1]-self.first[1])**2
        y =(self.second[0]-self.first[0])**2
        xy=(x+y)**0.5
        charge_per100meter=0.5
        total=charge_per100meter*xy
        total=int(total)




        pro.canvas.delete("all")
        pro.canvas.config(height=500,width=500)


        self.sucimg=PhotoImage(file="back.gif")
        pro.canvas.create_image(0,0,image=self.sucimg,anchor=NW)
        var=StringVar()

        welcome=Label(pro.canvas,text="BOOKING SUCCESSFULL",height=2,bg="#AED6F1",width=200,font="Helvetica 10 bold italic",fg="#FF4900")

        pro.canvas.create_window(250,20,window=welcome)

        amount="YOU NEED TO PAY AMOUNT OF "+str(total)+" RS"

        amountdisp= Label(pro.canvas, text=amount, height=2, width=200,bg="#AED6F1", font="Helvetica 10 bold italic", fg="#FF4900 ")
        pro.canvas.create_window(250, 80, window=amountdisp)



        waqt=self.time_entry.get()

            


        waqt="BE READY WITHIN 10 MIN WE ARE APPROACHING YOU "

        timelabel=Label(pro.canvas,text=waqt,height=5,width=200,bg="#AED6F1", font="Helvetica 10 bold italic", fg="#FF4900")
        pro.canvas.create_window(250,200,window=timelabel)

        qiut = Button(pro.canvas,  text="LOGOUT",bg="#06FCFC", relief="raised",fg="black",command=self.login, activebackground="red", cursor="hand1")
        pro.canvas.create_window(400,400,window=qiut)

        ANOTHER = Button(pro.canvas, text="ANOTHER BOOKINGS",relief="raised", bg="#06FCFC", fg="black", command=self.dashboard, activebackground="red",
                      cursor="hand1")
        pro.canvas.create_window(200, 400, window=ANOTHER)






    def dashboard(self):
            pro.canvas.config(height=650, width=800)
            pro.canvas.delete("all")

            self.dash=PhotoImage(file="dash.png")
            pro.canvas.create_image(80,0,image=self.dash,anchor=NW)
            la=Label(pro.canvas,text="LETS RIDE IN LPU",font="times 40 underline",fg="RED")
            pro.canvas.create_window(400,20,window=la)

            mlabel=Label(pro.canvas,text='MOBILE NO:',font="20",fg="GREEN")
            pro.canvas.create_window(250,200,window=mlabel)

            mentry=Entry(pro.canvas)
            pro.canvas.create_window(380,200,window=mentry)

        ########## places

            self.fromdict={"MAIN GATE":[0,0],"SHRI BALDEV RAJ HOSPITAL":[-200,300],
                      "BUSINESS-BLOCK":[-180,600],"ADMINISTARTION-BLOCK":[-170,800],"BLOCK 40-55":[-150,1600]}



            self.todict = {"MAIN GATE":[0,0],"SHRI BALDEV RAJ HOSPITAL":[-200,300],
            "BUSINESS-BLOCK":[-180,600],"ADMINISTARTION-BLOCK":[-170,800],"BLOCK 40-55":[-150,1600]}

            tup=self.fromdict.keys()
            tup=tuple(tup)

            totup = self.todict.keys()
            totup = tuple(totup)

            self.forcomo=ttk.Combobox(width=60)
            self.forcomo['values']=tup
            pro.canvas.create_window(500,250,window=self.forcomo)
            self.forcomo.bind("<<ComboboxSelected>>",self.fromm)

            from1 = Label(pro.canvas, text='FROM:', font="20", fg="GREEN")
            pro.canvas.create_window(250, 250, window=from1)

            to = Label(pro.canvas, text='TO:', font="20", fg="GREEN")
            pro.canvas.create_window(250, 300, window=to)





            self.newcomb=ttk.Combobox(width=60)
            self.newcomb['values']=totup
            pro.canvas.create_window(500,305,window=self.newcomb)
            self.newcomb.bind("<<ComboboxSelected>>",self.toplace)

            day = Label(pro.canvas, text='DAY', font="20", fg="GREEN")
            pro.canvas.create_window(250,355,window=day)



            days=("MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY")

            self.daycomb = ttk.Combobox(width=60)
            pro.canvas.create_window(500, 355, window=self.daycomb)
            self.daycomb['values']=days

            time = Label(pro.canvas, text="TIME:", font="20", fg="GREEN")
            pro.canvas.create_window(250,405, window=time)



            self.time_entry=Entry(pro.canvas)
            pro.canvas.create_window(370,405,window=self.time_entry)






            cal_fare=Button(pro.canvas,command=self.calculate_fare, text="CALCULATE FARE AND BOOK A CAB", background="#06FCFC", fg="black", activebackground="red",cursor="hand1")
            pro.canvas.create_window(420,500, window=cal_fare)
























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




        c=Button(pro.canvas, text="SUBMIT",command=valid, background="#06FCFC", fg="black", activebackground="red",cursor="hand1")
        pro.canvas.create_window(400,600, window=c)









s=pro()
s.login()
