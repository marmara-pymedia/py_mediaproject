from tkinter import *
from tkinter import font

class Login:
    def __init__(self,root) -> None:
        self.root=root

        self.loginFrame=Frame(self.root,bg="gray")
        self.loginFrame.pack(fill=BOTH,expand=True)
        self.loginChildFrame=Frame(self.loginFrame,bg="white")
        self.loginChildFrame.pack(expand=True,padx=250,pady=100,fill=BOTH)

        self.loginChild2Frame=Frame(self.loginChildFrame,bg='gray')
        self.loginChild2Frame.pack(padx=(5,5),pady=20,expand=True)

        self.usernameFrame=Frame(self.loginChild2Frame,bg="white")
        self.usernameFrame.grid(row=0,pady=50,padx=20)

        self.labelUsername=Label(self.usernameFrame,text="Username :")
        self.labelUsername.grid(row=0,column=0)

        self.entryUsername=Entry(self.usernameFrame,bg="gold")
        self.entryUsername.grid(row=0,column=1)

        self.passwordFrame=Frame(self.loginChild2Frame)
        self.passwordFrame.grid(row=1,column=0)

        self.labelPassword=Label(self.passwordFrame,text="Password :")
        self.labelPassword.grid(row=0,column=0)

        self.entryPassword=Entry(self.passwordFrame,bg="gold")
        self.entryPassword.grid(row=0,column=1)

        self.loginButtonFrame=Frame(self.loginChild2Frame)
        self.loginButtonFrame.grid(row=2,column=0,pady=50,padx=20)

        self.loginButton=Button(self.loginButtonFrame,text="Login",width=10,height=1)
        self.loginButton.pack(expand=True)

        while True:
            userName = input("Username: ")
            if (userName.isspace() != True):
                break
        while True:
            password = input("Password: ")
            if (password.isspace() != True):
                break
