from tkinter import *
import MySQLdb as m
from tkinter import messagebox


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.f = Frame(self.master, height=745, width=1295, bg='white')
        self.f.pack()

        self.lb = Label(self.f, text='Voting System', width=50, height=1, font=('Helvetics', 36, 'bold italic'),fg='black', bg='green')
        self.lb.place(x=0, y=0)

        self.db = m.connect(host="localhost", user="root", passwd="123456", db="election")
        self.cur = self.db.cursor()

        # Admin
        self.badmin = Button(self.f, text='ADMIN', width=8, height=2, font=('', 16, ''), fg='black', bg='green',
                             activeforeground='white', activebackground='grey')
        self.badmin.place(x=200, y=150)
        self.badmin.bind('<Button-1>', self.buttonClickadmin)

        # User
        self.buser = Button(self.f, text='USER', width=8, height=2, font=('', 16, ''), fg='black', bg='green',
                            activeforeground='white', activebackground='grey')
        self.buser.place(x=950, y=150)
        self.buser.bind('<Button-1>', self.buttonClickuser)

    def buttonClickadmin(self, master):
        self.fadmin = Frame(self.f, height=400, width=500, bg='white')
        self.fadmin.place(x=400, y=250)

        self.lbuser = Label(self.fadmin, text='Username : ', height=1, font=('', 22, ''), fg='black', bg='white')
        self.lbuser.place(x=0, y=60)

        self.euser = Entry(self.fadmin, width=30)
        self.euser.place(x=250, y=70)

        self.lbpass = Label(self.fadmin, text='Password : ', height=1, font=('', 22, ''), bg='white', fg='black')
        self.lbpass.place(x=0, y=160)
        self.epass = Entry(self.fadmin, width=15, show='*')
        self.epass.place(x=250, y=170)

        self.blogin = Button(self.fadmin, text='LOGIN', width=5, height=1, font=('', 16, ''), bg='green', fg='black',
                        activeforeground='white', activebackground='grey')
        self.blogin.place(x=200, y=280)
        self.blogin.bind('<Button-1>', self.buttonClicklogin)

    def buttonClicklogin(self, master):
        self.fp = open("login.txt", 'r')
        self.li = self.fp.readlines()
        self.flag = 0
        self.username = self.euser.get() + "\n"
        self.password = self.epass.get() + "\n"

        for i in range(0, len(self.li), 2):
            if (self.li[i] == self.username and self.li[i + 1] == self.password):
                self.flag = 1
                break

        if (self.flag == 0):
            print("Invalid username or password")
            self.lbmsg = Label(self.fadmin, text="Invalid username or password!", font=("", 12, ""), bg="white", fg="red")
            self.lbmsg.place(x=120, y=350)

        else:
            self.finfo = Frame(self.f, height=745, width=1295, bg="white")
            self.finfo.pack()
            self.xcor = 100
            self.ycor = 50

            self.cur.execute("SELECT * FROM results")
            self.rows = self.cur.fetchall()

            self.lhead1 = Label(self.finfo, text="NAME", font=("", 12, ""), bg="white", fg="black")
            self.lhead1.place(x=self.xcor, y=self.ycor)
            self.xcor += 350

            self.lhead2 = Label(self.finfo, text="ID NUMBER", font=("", 12, ""), bg="white", fg="black")
            self.lhead2.place(x=self.xcor, y=self.ycor)
            self.xcor += 200

            self.lhead3 = Label(self.finfo, text="AGE", font=("", 12, ""), bg="white", fg="black")
            self.lhead3.place(x=self.xcor, y=self.ycor)
            self.xcor += 100

            self.lhead4 = Label(self.finfo, text="GENDER", font=("", 12, ""), bg="white", fg="black")
            self.lhead4.place(x=self.xcor, y=self.ycor)
            self.xcor += 150

            self.lhead5 = Label(self.finfo, text="VOTE", font=("", 12, ""), bg="white", fg="black")
            self.lhead5.place(x=self.xcor, y=self.ycor)
            self.ycor += 20

            for row in self.rows:
                self.ycor += 25
                self.xcor = 100

                self.l1 = Label(self.finfo, text=row[0], font=("", 12, ""), bg="white", fg="black")
                self.l1.place(x=self.xcor, y=self.ycor)
                self.xcor += 350

                self.l2 = Label(self.finfo, text=row[1], font=("", 12, ""), bg="white", fg="black")
                self.l2.place(x=self.xcor, y=self.ycor)
                self.xcor += 200

                self.l3 = Label(self.finfo, text=row[2], font=("", 12, ""), bg="white", fg="black")
                self.l3.place(x=self.xcor, y=self.ycor)
                self.xcor += 100

                self.l4 = Label(self.finfo, text=row[3], font=("", 12, ""), bg="white", fg="black")
                self.l4.place(x=self.xcor, y=self.ycor)
                self.xcor += 150

                self.l5 = Label(self.finfo, text=row[4], font=("", 12, ""), bg="white", fg="black")
                self.l5.place(x=self.xcor, y=self.ycor)

                self.bstats = Button(self.finfo, text="STATE", width=5, height=1, font=("", 16, ""), bg="gold", fg="black",
                                activeforeground="white", activebackground="grey")
                self.bstats.place(x=510, y=650)
                self.bstats.bind('<Button-1>', self.buttonClickstats)

            self.bstats = Button(self.finfo, text="STATE", width=5, height=1, font=("", 16, ""), bg="gold", fg="black",
                            activeforeground="white", activebackground="grey")
            self.bstats.place(x=510, y=650)
            self.bstats.bind('<Button-1>', self.buttonClickstats)

            self.bback = Button(self.finfo, text="LOGOUT", width=7, height=1, font=("", 16, ""), bg="gold", fg="black",
                           activeforeground="white", activebackground="grey")
            self.bback.place(x=640, y=650)
            self.bback.bind('<Button-1>', self.buttonClickback)

    def buttonClickback(self, master):
        self.finfo.destroy()
        self.fadmin.destroy()

    def buttonClickstats(self, master):
        self.fstats = Frame(self.finfo, height=745, width=1295, bg="white")
        self.fstats.pack()
        self.xcor = 100
        self.ycor = 50

        self.cur.execute("SELECT * FROM countvotes") #need database
        self.rows = self.cur.fetchall()              #need database

        self.lhead1 = Label(self.fstats, text="PARTY", font=("", 12, ""), bg="white", fg="black")
        self.lhead1.place(x=self.xcor, y=self.ycor)
        self.xcor += 350
        self.lhead2 = Label(self.fstats, text="VOTES", font=("", 12, ""), bg="white", fg="black")
        self.lhead2.place(x=self.xcor, y=self.ycor)
        self.ycor += 20
        for row in self.rows:
            self.ycor += 25
            self.xcor = 100
            self.l1 = Label(self.fstats, text=row[0], font=("", 12, ""), bg="white", fg="black")
            self.l1.place(x=self.xcor, y=self.ycor)
            self.xcor += 350
            self.l2 = Label(self.fstats, text=row[1], font=("", 12, ""), bg="white", fg="black")
            self.l2.place(x=self.xcor, y=self.ycor)
            self.xcor += 200

        self.bexit = Button(self.fstats, text="BACK", width=5, height=1, font=("", 16, ""), bg="gold", fg="black",
                       activeforeground="white", activebackground="grey")
        self.bexit.place(x=600, y=650)
        self.bexit.bind('<Button-1>', self.buttonClickexit)

    def buttonClickexit(self, master):
        self.fstats.destroy()

    def buttonClickuser(self, master):
        self.fuser = Frame(self.f, height=400, width=500, bg='white')
        self.fuser.place(x=400, y=250)

        self.lbname = Label(self.fuser, text='Name : ', height=1, font=('', 22, ''), bg='white', fg='black')
        self.lbname.place(x=10, y=60)

        self.ename = Entry(self.fuser, width=25)
        self.ename.place(x=250, y=70)

        self.lbage = Label(self.fuser, text='Age : ', height=1, font=('', 22, ''), bg='white', fg='black')
        self.lbage.place(x=10, y=120)

        self.eage = Entry(self.fuser, width=3)
        self.eage.place(x=250, y=130)

        self.lbgen = Label(self.fuser, text='Gender : ', height=1, font=('', 22, ''), bg='white', fg='black')
        self.lbgen.place(x=10, y=180)

        self.varg = IntVar()
        self.rmale = Radiobutton(self.fuser, variable=self.varg, value=1, text=' Male', font=('', 12, ''), fg='Black', bg='White')
        self.rmale.place(x=250, y=190)

        self.rfem = Radiobutton(self.fuser, variable=self.varg, value=2, text=' Female', font=('', 12, ''), fg='Black', bg='White')
        self.rfem.place(x=350, y=190)

        self.lbadh = Label(self.fuser, text="ID NO. : ", height=1, font=("", 22, ""), bg="white", fg="black")
        self.lbadh.place(x=10, y=240)

        self.eid = Entry(self.fuser, width=12)
        self.eid.place(x=250, y=250)

        self.bsub = Button(self.fuser, text='SUBMIT', width=5, height=1, font=('', 16, ''), fg='black', bg='green',
                      activeforeground='white', activebackground='grey')
        self.bsub.place(x=200, y=320)
        self.bsub.bind('<Button-1>', self.buttonClicksub)

    def buttonClicksub(self, master):
        self.name = self.ename.get()
        self.age = self.eage.get()
        self.id = self.eid.get()
        self.vote = "None"

        if (self.varg.get() == 1):
            self.gender = "Male"
        else:
            self.gender = "Female"

        self.check = 1

        if (len(self.id) < 12):
            check = 0

        if (self.age < "18"):
            self.check = 0

        try:
            tmp = float(self.eid.get())
        except ValueError:
            check = 0

        try:
            tmp = int(self.eage.get())
        except ValueError:
            check = 0

        if (self.check == 0):
            self.lbmsg = Label(self.fuser, text="Invalid details!", font=("", 12, ""), bg="white", fg="red")
            self.lbmsg.place(x=190, y=370)
        else:
            self.fvote = Frame(self.f, height=745, width=1295, bg='white')
            self.fvote.pack()

            self.lb = Label(self.fvote, text='Voting System', width=50, height=1, font=('Helvetica', 36, 'bold italic'), fg='black',
                       bg='green')
            self.lb.place(x=0, y=0)

            self.lbtitle = Label(self.fvote, text='Candidate List', height=1, font=('', 22, 'bold underline'), bg='white', fg='black')
            self.lbtitle.place(x=180, y=100)

            self.lbvote = Label(self.fvote, text='Vote', height=1, font=('', 22, 'bold underline'), bg='white', fg='black')
            self.lbvote.place(x=950, y=100)

            self.vargv = IntVar()

            self.lb1 = Label(self.fvote, text='Java', height=1, font=('', 16, ''), bg='white', fg='black')
            self.lb1.place(x=200, y=180)

            self.r1 = Radiobutton(self.fvote, variable=self.vargv, value=1, bg='white', fg='Black')
            self.r1.place(x=970, y=180)

            self.lb2 = Label(self.fvote, text='Python', height=1, font=('', 16, ''), bg='white', fg='black')
            self.lb2.place(x=200, y=260)

            self.r2 = Radiobutton(self.fvote, variable=self.vargv, value=2, bg='white', fg='Black')
            self.r2.place(x=970, y=260)

            self.lb3 = Label(self.fvote, text='C++', height=1, font=('', 16, ''), bg='white', fg='black')
            self.lb3.place(x=200, y=340)

            self.r3 = Radiobutton(self.fvote, variable=self.vargv, value=3, bg='white', fg='Black')
            self.r3.place(x=970, y=340)

            self.lb4 = Label(self.fvote, text='HTML', height=1, font=('', 16, ''), bg='white', fg='black')
            self.lb4.place(x=200, y=420)

            self.r4 = Radiobutton(self.fvote, variable=self.vargv, value=4, bg='white', fg='Black')
            self.r4.place(x=970, y=420)

            self.lb5 = Label(self.fvote, text='R', height=1, font=('', 16, ''), bg='white', fg='black')
            self.lb5.place(x=200, y=500)

            self.r5 = Radiobutton(self.fvote, variable=self.vargv, value=5, bg='white', fg='Black')
            self.r5.place(x=970, y=500)

            self.lb6 = Label(self.fvote, text='JavaScript', height=1, font=('', 16, ''), bg='white', fg='black')
            self.lb6.place(x=200, y=580)

            self.r6 = Radiobutton(self.fvote, variable=self.vargv, value=6, bg='white', fg='Black')
            self.r6.place(x=970, y=580)

            self.bcast = Button(self.fvote, text="SUBMIT", width=5, height=1, font=("", 16, ""), bg="gold", fg="black",
                           activeforeground="white", activebackground="grey")
            self.bcast.place(x=600, y=650)
            self.bcast.bind('<Button-1>', self.buttonClickcast)

    def buttonClickcast(self, master):
        try:
            self.val = self.vargv.get()
        except UnboundLocalError:
            self.val = 7

        if (self.val == 1):
            self.vote = "Java"

        elif (self.val == 2):
            self.vote = "Python"

        elif (self.val == 3):
            self.vote = "C++"

        elif (self.val == 4):
            self.vote = "HTML"

        elif (self.val == 5):
            self.vote = "R"

        elif (self.val == 6):
            self.vote = "JavaScript"

        else:
            self.vote = "NONE"

        self.cur.execute("Insert into results (name,id, age,gender,vote) Values(%s,%s,%s,%s,%s)",
                        (self.name, self.id, self.age, self.gender, self.vote))
        self.cur.execute("commit;")
        self.cur.execute("UPDATE countvotes SET count=count+1 WHERE name='%s'" % (self.vote))
        self.cur.execute("commit;")
        self.fvote.destroy()
        self.fuser.destroy()