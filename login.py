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

        #getting all users from the database
        self.user_service=self.controller.main_service.user_service
        self.all_users=self.user_service.get_all()

        #login page design starts here, login frames created
        self.login_frame=Frame(self.root,bg="#070F2B",width=1920,height=1080)
        self.login_frame.pack(fill=BOTH,expand=True)
        self.login_frame.pack_propagate(False)

        self.login_child_frame=Frame(self.login_frame,bg="#1B1A55")
        self.login_child_frame.pack(expand=True,padx=709,pady=146,fill=BOTH)

        self.login_child_2_frame=Frame(self.login_child_frame,bg='#1B1A55')
        self.login_child_2_frame.pack(padx=56,pady=(108,109),expand=True)

        #logo frame created
        self.logo_frame=Frame(self.login_child_2_frame)
        self.logo_frame.grid(row=0,column=0,padx=150,pady=15)

        #logo image added to the logo frame
        self.logo=PhotoImage(file="medias/logos/loginLogo.png")
        self.logo_label=Label(self.logo_frame,image=self.logo)
        self.logo_label.pack(fill=BOTH)

        #username frame, label and entry created
        self.username_frame=Frame(self.login_child_2_frame,bg="#535C91")
        self.username_frame.grid(row=1,pady=(20,10))

        self.label_username=Label(self.username_frame,text="Username :",font=("Roboto",20),bg="#535C91",fg="white")
        self.label_username.grid(row=0,column=0,padx=(5,5))

        self.entry_username=Entry(self.username_frame,bg="white",font=("Roboto",16),width=15) #getting the username from the user
        self.entry_username.grid(row=0,column=1,padx=(5,5))

        #password frame, label and entry created
        self.password_frame=Frame(self.login_child_2_frame,bg="#535C91")
        self.password_frame.grid(row=2,pady=10)

        self.label_password=Label(self.password_frame,text="Password :",font=("Roboto",20),bg="#535C91",fg="white")
        self.label_password.grid(row=0,column=0,padx=(5,5))

        self.entry_password=Entry(self.password_frame,bg="white",font=("Roboto",16),width=15,show="*") #getting the password from the user and showing it as *
        self.entry_password.grid(row=0,column=1,padx=(5,5))

        #login button frame and button created
        self.login_button_frame=Frame(self.login_child_2_frame, bg="#535C91")
        self.login_button_frame.grid(row=3,pady=15)

        self.login_button=Button(self.login_button_frame,text="Login",font=("Roboto",15),bg="#535C91",fg="white",width=10,height=1,cursor="hand2", command=self.control_fields_login) #when clicked, control_fields_login function will be called
        self.login_button.pack(expand=True)

        #register frame and labels created
        self.register_frame=Frame(self.login_child_2_frame,bg="#1B1A55")
        self.register_frame.grid(row=4,pady=25)

        self.register_label_1=Label(self.register_frame,text="Don't have an account?",font=("Roboto",16),fg="black")
        self.register_label_1.grid(row=0,column=0)

        self.register_label_2=Label(self.register_frame,text="Register.",font=("Roboto",16),fg="blue",cursor="hand2")
        self.register_label_2.grid(row=0,column=1)
        self.register_label_2.bind("<Button-1>", lambda e: self.switch_to_register_page()) #when clicked, switch_to_register_page function will be called

        #frames created
        self.fram1=Frame(self.root,bg="#070F2B")
        self.fram1.pack(expand=True,padx=709,pady=900,fill=BOTH)

        self.frame2=Frame(self.root,bg="#070F2B")
        self.frame2.pack(expand=True,padx=600,pady=900,fill=BOTH)

    # def destroy(self):
    #     self.login_frame.destroy()

    #login function
    def login(self):
        self.controller.user=None

    #switch to register page function
    def switch_to_register_page(self):
        self.controller.show_register_page()

    #control fields function
    def control_fields_login(self):
        username = self.entry_username.get().strip()
        password = self.entry_password.get().strip()

        #checking if the fields are empty, checking if the user is in the database
        #if the user is in the database, showing the home page to the user and if the user is not in the database, showing an error message to the user
        if not username or not password:
            messagebox.showerror("Error", "All fields are required!")
            return
        else:
            for user in self.all_users:
                if user.user_name==username and user.password==password:
                    self.controller.user=user
                print(user.user_name,user.password)
            print(username,password)
            print(self.controller.user)
            print("User found!")
            if self.controller.user!=None:
                self.controller.show_home_page()
            else:
                messagebox.showerror("Error", "User not found!")

