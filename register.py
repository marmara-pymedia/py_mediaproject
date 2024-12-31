import re
import json
from tkinter import messagebox
from entities.User import User
from services.UserService import UserService
from tkinter import *
from tkinter import font
from tkinter import PhotoImage
from tkinter import messagebox
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from login import Login

class Register(Frame):

    def __init__(self, root,controller) -> None:
        Frame.__init__(self,root)
        self.root=self
        self.controller=controller
        self.user_service=UserService()
        self.all_users=self.user_service.get_all()

        print("Register")

        self.register_frame=Frame(self.root,bg="#070F2B")
        self.register_frame.pack(fill=BOTH,expand=True)
        self.register_child_frame=Frame(self.register_frame,bg="#1B1A55")
        self.register_child_frame.pack(expand=True,padx=709,pady=146,fill=BOTH)

        self.register_child_2_frame=Frame(self.register_child_frame,bg='#1B1A55')
        self.register_child_2_frame.pack(padx=56,pady=(80,109),expand=True)


        self.logo_register_frame=Frame(self.register_child_2_frame)
        self.logo_register_frame.grid(row=0,column=0,padx=150,pady=15)

        self.logo_register=PhotoImage(file="medias\logos\\loginLogo.png")
        self.logo_register_label=Label(self.logo_register_frame,image=self.logo_register)
        self.logo_register_label.pack(fill=BOTH)


        self.first_name_frame=Frame(self.register_child_2_frame,bg="#535C91")
        self.first_name_frame.grid(row=1,pady=(20,10))

        self.label_first_name=Label(self.first_name_frame,text="First Name :",font=("Roboto",20),bg="#535C91",fg="white")
        self.label_first_name.grid(row=0,column=0,padx=(5,5))

        self.entry_first_name=Entry(self.first_name_frame,bg="white",font=("Roboto",16),width=15)
        self.entry_first_name.grid(row=0,column=1,padx=(5,5))


        self.last_name_frame=Frame(self.register_child_2_frame,bg="#535C91")
        self.last_name_frame.grid(row=2,pady=10)

        self.label_last_name=Label(self.last_name_frame,text="Last Name :",font=("Roboto",20),bg="#535C91",fg="white")
        self.label_last_name.grid(row=0,column=0,padx=(5,5))

        self.entry_last_name=Entry(self.last_name_frame,bg="white",font=("Roboto",16),width=15)
        self.entry_last_name.grid(row=0,column=1,padx=(5,5))


        self.username_frame=Frame(self.register_child_2_frame,bg="#535C91")
        self.username_frame.grid(row=3,pady=10)

        self.label_username=Label(self.username_frame,text="Username :",font=("Roboto",20),bg="#535C91",fg="white")
        self.label_username.grid(row=0,column=0,padx=(5,5))

        self.entry_username=Entry(self.username_frame,bg="white",font=("Roboto",16),width=15)
        self.entry_username.grid(row=0,column=1,padx=(5,5))


        self.password_frame=Frame(self.register_child_2_frame,bg="#535C91")
        self.password_frame.grid(row=4,pady=10)

        self.label_password=Label(self.password_frame,text="Password :",font=("Roboto",20),bg="#535C91",fg="white")
        self.label_password.grid(row=0,column=0,padx=(5,5))

        self.entry_password=Entry(self.password_frame,bg="white",font=("Roboto",16),width=15)
        self.entry_password.grid(row=0,column=1,padx=(5,5))


        self.register_button_frame=Frame(self.register_child_2_frame,bg="#535C91")
        self.register_button_frame.grid(row=5,pady=15)

        self.register_button=Button(self.register_button_frame,text="Register",font=("Roboto",15),bg="#535C91",fg="white",width=10,height=1,cursor="hand2", command=self.control_fields)
        self.register_button.pack(expand=True)

        self.back_button_frame=Frame(self.register_child_2_frame,bg="white")
        self.back_button_frame.grid(row=6,column=0,pady=(0,10))

        self.back_button=Button(self.back_button_frame,text="Back",font=("Roboto",15),bg="white",fg="black",width=10,height=1,cursor="hand2", command=self.switch_to_login_page)
        self.back_button.pack(expand=True)

    def switch_to_login_page(self):
        self.controller.show_frame(Login)

    def control_fields(self):
        first_name = self.entry_first_name.get().strip()
        last_name = self.entry_last_name.get().strip()
        username = self.entry_username.get().strip()
        password = self.entry_password.get().strip()

        symbols = "!@#$%^&*()_+-=[]{}|;:'\",.<>?/"

        if not first_name or not last_name or not username or not password:
            messagebox.showerror("Error", "All fields are required!")
            return
        
        if not first_name.isalpha():
            messagebox.showerror("Error", "First Name must consist of only letters!")
            return
        
        if not last_name.isalpha():
            messagebox.showerror("Error", "Last Name must consist of only letters!")
            return

        if not username.isalnum():
            messagebox.showerror("Error", "Username must consist of only letters and numbers!")
            return
        elif self.user_service.get_user_by_id(username):
            messagebox.showerror("Error", "This username already exists!")
            return
        # else:
        #     self.all_users.append(username)

        if len(password)<8:
            messagebox.showerror("Error", "Password must be at least 8 characters long!")
            return
        if not re.search(r'[A-Z]', password):
            messagebox.showerror("Error", "Password must contain at least one uppercase letter!")
            return
        if not re.search(r'[a-z]', password):
            messagebox.showerror("Error", "Password must contain at least one lowercase letter!")
            return
        if not re.search(r'\d', password):
            messagebox.showerror("Error", "Password must contain at least one number!")
            return
        if not any(char in symbols for char in password):
            messagebox.showerror("Error", f"Password must contain at least one special characters: {symbols}")

        user=User(first_name,last_name,username,password)
        self.register(user)
        messagebox.showinfo("Successful", f"Username '{username}' is successfully saved!")


    def register(self,user:User):
        userService=UserService()
        userService.addUser(user)
        print(user.firstName,"kayit basarili")