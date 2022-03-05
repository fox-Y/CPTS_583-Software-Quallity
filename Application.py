from tkinter import *
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
        pass

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

        self.bsub = Button(self.fuser, text='SUBMIT', width=5, height=1, font=('', 16, ''), fg='black', bg='green',
                      activeforeground='white', activebackground='grey')
        self.bsub.place(x=200, y=320)
        self.bsub.bind('<Button-1>', self.buttonClicksub)

    def buttonClicksub(self, master):
        pass