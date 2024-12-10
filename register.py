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

        self.registerFrame=Frame(self.root,bg="gray")
        self.registerFrame.pack(fill=BOTH,expand=True)
        self.registerChildFrame=Frame(self.registerFrame,bg="white")
        self.registerChildFrame.pack(expand=True,padx=709,pady=146,fill=BOTH)

        self.registerChild2Frame=Frame(self.registerChildFrame,bg='gray')
        self.registerChild2Frame.pack(padx=56,pady=(108,109),expand=True)


        self.logoRegisterFrame=Frame(self.registerChild2Frame)
        self.logoRegisterFrame.grid(row=0,column=0,padx=150,pady=15)

        self.logoRegister=PhotoImage(file="medias\logos\loginLogo.png")
        self.logoRegisterLabel=Label(self.logoRegisterFrame,image=self.logoRegister)
        self.logoRegisterLabel.pack(fill=BOTH)


        self.firstNameFrame=Frame(self.registerChild2Frame,bg="white")
        self.firstNameFrame.grid(row=1)

        self.labelFirstName=Label(self.firstNameFrame,text="First Name :",font=("Roboto",14))
        self.labelFirstName.grid(row=0,column=0)

        self.entryFirstName=Entry(self.firstNameFrame,bg="gold")
        self.entryFirstName.grid(row=0,column=1)


        self.lastNameFrame=Frame(self.registerChild2Frame)
        self.lastNameFrame.grid(row=2,pady=10)

        self.labelLastName=Label(self.lastNameFrame,text="Last Name :",font=("Roboto",14))
        self.labelLastName.grid(row=0,column=0)

        self.entryLastName=Entry(self.lastNameFrame,bg="gold")
        self.entryLastName.grid(row=0,column=1)


        self.usernameFrame=Frame(self.registerChild2Frame)
        self.usernameFrame.grid(row=3,pady=10)

        self.labelUsername=Label(self.usernameFrame,text="Username :",font=("Roboto",14))
        self.labelUsername.grid(row=0,column=0)

        self.entryUsername=Entry(self.usernameFrame,bg="gold")
        self.entryUsername.grid(row=0,column=1)


        self.passwordFrame=Frame(self.registerChild2Frame)
        self.passwordFrame.grid(row=4,pady=10)

        self.labelPassword=Label(self.passwordFrame,text="Password :",font=("Roboto",14))
        self.labelPassword.grid(row=0,column=0)

        self.entryPassword=Entry(self.passwordFrame,bg="gold")
        self.entryPassword.grid(row=0,column=1)


        self.registerButtonFrame=Frame(self.registerChild2Frame)
        self.registerButtonFrame.grid(row=5)

        self.registerButton=Button(self.registerButtonFrame,text="Register",width=10,height=1,cursor="hand2", command=self.control_fields)
        self.registerButton.pack(expand=True)

    def control_fields(self):
        first_name = self.entryFirstName.get().strip()
        last_name = self.entryLastName.get().strip()
        username = self.entryUsername.get().strip()
        Password = self.entryPassword.get().strip()

        symbols = "!@#$%^&*()_+-=[]{}|;:'\",.<>?/"

        if not first_name or not last_name or not username or not Password:
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

        if len(Password)<8:
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

        user=User(first_name,last_name,username,Password)
        self.register(user)


    def register(self,user:User):
        userService=UserService()
        userService.addUser(user)
        print(user.firstName,"kayit basarili")