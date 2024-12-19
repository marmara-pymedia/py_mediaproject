from tkinter import *
from tkinter import font
from tkinter import PhotoImage
from register import Register

class Login:
    def __init__(self,root) -> None:
        self.root=root

        self.login_frame=Frame(self.root,bg="#070F2B")
        self.login_frame.pack(fill=BOTH,expand=True)
        self.login_child_frame=Frame(self.login_frame,bg="#535C91")
        self.login_child_frame.pack(expand=True,padx=709,pady=146,fill=BOTH)

        self.login_child_2_frame=Frame(self.login_child_frame,bg='#9290C3')
        self.login_child_2_frame.pack(padx=56,pady=(108,109),expand=True)

        self.logo_frame=Frame(self.login_child_2_frame)
        self.logo_frame.grid(row=0,column=0,padx=150,pady=34)

        self.logo=PhotoImage(file="medias\logos\loginLogo.png")
        self.logo_label=Label(self.logo_frame,image=self.logo)
        self.logo_label.pack(fill=BOTH)


        self.username_frame=Frame(self.login_child_2_frame,bg="#9290C3")
        self.username_frame.grid(row=1)

        self.label_username=Label(self.username_frame,text="Username :",font=("Roboto",14),bg="#9290C3",fg="#d8c4b6")
        self.label_username.grid(row=0,column=0)

        self.entry_username=Entry(self.username_frame,bg="gold")
        self.entry_username.grid(row=0,column=1)

        self.password_frame=Frame(self.login_child_2_frame,bg="#9290C3")
        self.password_frame.grid(row=2,pady=25)

        self.label_password=Label(self.password_frame,text="Password :",font=("Roboto",14),bg="#9290C3",fg="#d8c4b6")
        self.label_password.grid(row=0,column=0)

        self.entry_password=Entry(self.password_frame,bg="gold")
        self.entry_password.grid(row=0,column=1)

        self.login_button_frame=Frame(self.login_child_2_frame, bg="#535C91")
        self.login_button_frame.grid(row=3)

        self.login_button=Button(self.login_button_frame,text="Login",width=10,height=1,cursor="hand2")
        self.login_button.pack(expand=True)

        self.register_frame=Frame(self.login_child_2_frame,bg="#9290C3")
        self.register_frame.grid(row=4,pady=25)

        self.register_label_1=Label(self.register_frame,text="Hesabınız yok mu?",fg="#d8c4b6")
        self.register_label_1.grid(row=0,column=0)

        self.register_label_2=Label(self.register_frame,text="Kayıt ol.",fg="blue",cursor="hand2")
        self.register_label_2.grid(row=0,column=1)
        self.register_label_2.bind("<Button-1>", lambda e: self.switch_to_register_page)


        self.fram1=Frame(self.root,bg="#070F2B")
        self.fram1.pack(expand=True,padx=709,pady=900,fill=BOTH)

        self.frame2=Frame(self.root,bg="#070F2B")
        self.frame2.pack(expand=True,padx=600,pady=900,fill=BOTH)



        while True:
            userName = input("Username: ")
            if (userName.isspace() != True):
                break
        while True:
            password = input("Password: ")
            if (password.isspace() != True):
                break

    def switch_to_register_page(self):
        Register()

