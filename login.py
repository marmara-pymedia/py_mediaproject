from tkinter import *
from tkinter import font
from tkinter import PhotoImage
from register import Register

class Login:
    def __init__(self,root) -> None:
        self.root=root

        self.loginFrame=Frame(self.root,bg="gray")
        self.loginFrame.pack(fill=BOTH,expand=True)
        self.loginChildFrame=Frame(self.loginFrame,bg="white")
        self.loginChildFrame.pack(expand=True,padx=709,pady=146,fill=BOTH)

        self.loginChild2Frame=Frame(self.loginChildFrame,bg='gray')
        self.loginChild2Frame.pack(padx=56,pady=(108,109),expand=True)

        self.logoFrame=Frame(self.loginChild2Frame)
        self.logoFrame.grid(row=0,column=0,padx=150,pady=34)

        self.logo=PhotoImage(file="medias\logos\loginLogo.png")
        self.logoLabel=Label(self.logoFrame,image=self.logo)
        self.logoLabel.pack(fill=BOTH)


        self.usernameFrame=Frame(self.loginChild2Frame,bg="white")
        self.usernameFrame.grid(row=1)

        self.labelUsername=Label(self.usernameFrame,text="Username :",font=("Roboto",14))
        self.labelUsername.grid(row=0,column=0)

        self.entryUsername=Entry(self.usernameFrame,bg="gold")
        self.entryUsername.grid(row=0,column=1)

        self.passwordFrame=Frame(self.loginChild2Frame)
        self.passwordFrame.grid(row=2,pady=25)

        self.labelPassword=Label(self.passwordFrame,text="Password :",font=("Roboto",14))
        self.labelPassword.grid(row=0,column=0)

        self.entryPassword=Entry(self.passwordFrame,bg="gold")
        self.entryPassword.grid(row=0,column=1)

        self.loginButtonFrame=Frame(self.loginChild2Frame)
        self.loginButtonFrame.grid(row=3)

        self.loginButton=Button(self.loginButtonFrame,text="Login",width=10,height=1,cursor="hand2")
        self.loginButton.pack(expand=True)

        self.registerFrame=Frame(self.loginChild2Frame)
        self.registerFrame.grid(row=4,pady=25)

        self.registerLabel1=Label(self.registerFrame,text="Hesabınız yok mu?")
        self.registerLabel1.grid(row=0,column=0)

        self.registerLabel2=Label(self.registerFrame,text="Kayıt ol.",fg="blue",cursor="hand2")
        self.registerLabel2.grid(row=0,column=1)
        self.registerLabel2.bind("<Button-1>", lambda e: self.switchToRegisterPage)



        while True:
            userName = input("Username: ")
            if (userName.isspace() != True):
                break
        while True:
            password = input("Password: ")
            if (password.isspace() != True):
                break

    def switchToRegisterPage(self):
        Register()

