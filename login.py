from tkinter import *
from tkinter import font
from tkinter import PhotoImage
from tkinter import messagebox
from homePage import HomePage
from register import Register
from services.UserService import UserService
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from register import Register

class Login(Frame):
    def __init__(self,root,controller) -> None:
        Frame.__init__(self,root)
        self.root=self
        self.controller=controller
        self.user_service=UserService()
        self.all_users=self.user_service.get_all()

        self.login_frame=Frame(self.root,bg="#070F2B",width=1920,height=1080)
        self.login_frame.pack(fill=BOTH,expand=True)
        self.login_frame.pack_propagate(False)
        self.login_child_frame=Frame(self.login_frame,bg="#1B1A55")
        self.login_child_frame.pack(expand=True,padx=709,pady=146,fill=BOTH)

        self.login_child_2_frame=Frame(self.login_child_frame,bg='#1B1A55')
        self.login_child_2_frame.pack(padx=56,pady=(108,109),expand=True)

        self.logo_frame=Frame(self.login_child_2_frame)
        self.logo_frame.grid(row=0,column=0,padx=150,pady=15)

        self.logo=PhotoImage(file="medias\logos\\loginLogo.png")
        self.logo_label=Label(self.logo_frame,image=self.logo)
        self.logo_label.pack(fill=BOTH)


        self.username_frame=Frame(self.login_child_2_frame,bg="#535C91")
        self.username_frame.grid(row=1,pady=(20,10))

        self.label_username=Label(self.username_frame,text="Username :",font=("Roboto",20),bg="#535C91",fg="white")
        self.label_username.grid(row=0,column=0,padx=(5,5))

        self.entry_username=Entry(self.username_frame,bg="white",font=("Roboto",16),width=15)
        self.entry_username.grid(row=0,column=1,padx=(5,5))

        self.password_frame=Frame(self.login_child_2_frame,bg="#535C91")
        self.password_frame.grid(row=2,pady=10)

        self.label_password=Label(self.password_frame,text="Password :",font=("Roboto",20),bg="#535C91",fg="white")
        self.label_password.grid(row=0,column=0,padx=(5,5))

        self.entry_password=Entry(self.password_frame,bg="white",font=("Roboto",16),width=15)
        self.entry_password.grid(row=0,column=1,padx=(5,5))

        self.login_button_frame=Frame(self.login_child_2_frame, bg="#535C91")
        self.login_button_frame.grid(row=3,pady=15)

        self.login_button=Button(self.login_button_frame,text="Login",font=("Roboto",15),bg="#535C91",fg="white",width=10,height=1,cursor="hand2", command=self.control_fields_login)
        self.login_button.pack(expand=True)

        self.register_frame=Frame(self.login_child_2_frame,bg="#1B1A55")
        self.register_frame.grid(row=4,pady=25)

        self.register_label_1=Label(self.register_frame,text="Don't have an account?",font=("Roboto",16),fg="black")
        self.register_label_1.grid(row=0,column=0)

        self.register_label_2=Label(self.register_frame,text="Register.",font=("Roboto",16),fg="blue",cursor="hand2")
        self.register_label_2.grid(row=0,column=1)
        self.register_label_2.bind("<Button-1>", lambda e: self.switch_to_register_page())


        self.fram1=Frame(self.root,bg="#070F2B")
        self.fram1.pack(expand=True,padx=709,pady=900,fill=BOTH)

        self.frame2=Frame(self.root,bg="#070F2B")
        self.frame2.pack(expand=True,padx=600,pady=900,fill=BOTH)

    # def destroy(self):
    #     self.login_frame.destroy()

    def login(self):
        self.controller.user=None

    def switch_to_register_page(self):
        self.controller.show_frame(Register)

    def control_fields_login(self):
        username = self.entry_username.get().strip()
        password = self.entry_password.get().strip()

        if not username or not password:
            messagebox.showerror("Error", "All fields are required!")
            return
        elif not username:
            messagebox.showerror("Error", "Username cannot be empty!")
        elif not password:
            messagebox.showerror("Error", "Password cannot be empty!")
        elif not username.isalnum():
            messagebox.showerror("Error", "Username must consist only letters and numbers!")
        elif not password.isalnum():
            messagebox.showerror("Error", "Password must consist only letters and numbers!")
        elif not self.user_service.get_user_by_id(username):
            messagebox.showerror("Error", "User not found!")
        elif self.user_service.get_user_by_id(username).password != password:
            messagebox.showerror("Error", "Password is incorrect!")
        else:
            self.controller.user = self.user_service.get_user_by_id(username)
            self.controller.show_frame(HomePage)
        

        
        #self.user_service.add_user(User(username,password))
