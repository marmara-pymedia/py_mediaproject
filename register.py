import re
import json
from tkinter import messagebox
from entities.User import User
from services.UserService import UserService
from tkinter import *
from tkinter import font
from tkinter import PhotoImage

class Register:

    def __init__(self, root) -> None:
        self.root=root
        print("Register")

        self.register_frame=Frame(self.root,bg="#070F2B")
        self.register_frame.pack(fill=BOTH,expand=True)
        self.register_child_frame=Frame(self.register_frame,bg="#1B1A55")
        self.register_child_frame.pack(expand=True,padx=709,pady=146,fill=BOTH)

        self.register_child_2_frame=Frame(self.register_child_frame,bg='#1B1A55')
        self.register_child_2_frame.pack(padx=56,pady=(80,109),expand=True)


        self.logo_register_frame=Frame(self.register_child_2_frame)
        self.logo_register_frame.grid(row=0,column=0,padx=150,pady=15)

        self.logo_register=PhotoImage(file="medias\logos\loginLogo.png")
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

    def control_fields(self):
        first_name = self.entry_first_name.get().strip()
        last_name = self.entry_last_name.get().strip()
        username = self.entry_username.get().strip()
        password = self.entry_password.get().strip()

        symbols = "!@#$%^&*()_+-=[]{}|;:'\",.<>?/"

        if not first_name or not last_name or not username or not password:
            messagebox.showerror("Error", "All fields are required!")
            return
        
        if not all(char.isalpha() for char in first_name):
            messagebox.showerror("Error", "First Name must consist only letters!")

        if not all(char.isalpha() for char in last_name):
            messagebox.showerror("Hata", "Last Name must consist only letters!")

        if not username:
            messagebox.showerror("Error", "Username cannot be empty!")
        elif not username.isalnum():
            messagebox.showerror("Error", "Username must consist only letters and numbers!")
        elif username in existing_usernames:  #burada existing_usernames değişmeli!!!!
            messagebox.showerror("Error", "This username already exists!")
        else:
            existing_usernames.append(username)
            messagebox.showinfo("Successful", f"Username '{username}' is successfully saved!")

        if len(password)<8:
            messagebox.showerror("Error", "Password must be longer than 8 characters!")
        elif not re.search(r'[A-Z]', password):
            messagebox.showerror("Error", "Password must consist at least an upper case letter!")
        elif not re.search(r'[a-z]', password):
            messagebox.showerror("Error", "Password must consist at least a lower case letter!")
        elif not re.search(r'\d', password):
            messagebox.showerror("Error", "Password must consist at least a number!")
        elif not any(char in symbols for char in password):
            messagebox.showerror("Error", f"Password must consist at least one of these special characters: {symbols}")
        else:
            messagebox.showinfo("Successful", "Password valid!")

        user=User(first_name,last_name,username,password)
        self.register(user)


    def register(self,user:User):
        userService=UserService()
        userService.addUser(user)
        print(user.firstName,"kayit basarili")