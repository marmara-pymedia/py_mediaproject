from tkinter import filedialog, messagebox
from entities.User import User
from services.UserService import UserService
from tkinter import *
from tkinter import font
from tkinter import PhotoImage
from register import Register
import shutil

class UserProfile(Frame):

    def __init__(self, root,controller) -> None:
        Frame.__init__(self,root)
        self.root=self
        self.controller=controller
        self.user_name=self.controller.user.user_name
        self.first_name=self.controller.user.first_name
        self.last_name=self.controller.user.last_name
        self.user_service=self.controller.main_service.user_service
        self.big_img_path = ""
        self.small_img_path = ""
        self.all_users=self.user_service.get_all()


        self.user_profile_frame=Frame(self.root,bg="#070F2B")
        self.user_profile_frame.pack(fill=BOTH,expand=True)

        self.user_profile_child_frame=Frame(self.user_profile_frame,bg="#1B1A55")
        self.user_profile_child_frame.pack(expand=True)

        self.user_profile_child2_frame=Frame(self.user_profile_child_frame,bg='#1B1A55')
        self.user_profile_child2_frame.pack(padx=100,pady=55,expand=True)

        self.logo_user_profile_frame=Frame(self.user_profile_child2_frame, bg="#535C91",height=200,width=200)
        self.logo_user_profile_frame.grid(row=0,column=0,padx=150,pady=15) 
        self.logo_user_profile_frame.pack_propagate(False)
        self.logo_user_profile_frame.grid_propagate(False)
        
        self.logo_user_profile=PhotoImage(file=self.controller.user.big_image_path)
        self.logo_user_profile_label=Label(self.logo_user_profile_frame,image=self.logo_user_profile)
        self.logo_user_profile_label.img_reference=self.logo_user_profile
        self.logo_user_profile_label.pack(fill=BOTH)

        self.username_frame=Frame(self.user_profile_child2_frame,bg="#1B1A55")
        self.username_frame.grid(row=1,pady=30)

        self.label_username=Label(self.username_frame,text="Username",font=("Roboto",20),bg="#1B1A55",fg="#D8C4B6")
        self.label_username.grid(row=0,column=0)

        self.label_username_get=Label(self.username_frame,text=self.user_name,font=("Roboto",24),bg="#1B1A55",fg="#D8C4B6")
        self.label_username_get.grid(row=1,column=0)


        self.first_name_frame=Frame(self.user_profile_child2_frame,bg="#1B1A55")
        self.first_name_frame.grid(row=2,pady=30)

        self.label_first_name=Label(self.first_name_frame,text="First Name",font=("Roboto",20),bg="#1B1A55",fg="#D8C4B6")
        self.label_first_name.grid(row=0,column=0)

        self.label_first_name_get=Label(self.first_name_frame,text=self.first_name,font=("Roboto",24),bg="#1B1A55",fg="#D8C4B6")
        self.label_first_name_get.grid(row=1,column=0)


        self.last_name_frame=Frame(self.user_profile_child2_frame,bg="#1B1A55")
        self.last_name_frame.grid(row=3,pady=30)

        self.label_last_name=Label(self.last_name_frame,text="Last Name",font=("Roboto",20),bg="#1B1A55",fg="#D8C4B6")
        self.label_last_name.grid(row=0,column=0)

        self.label_last_name_get=Label(self.last_name_frame,text=self.last_name,font=("Roboto",24),bg="#1B1A55",fg="#D8C4B6")
        self.label_last_name_get.grid(row=1,column=0)

        self.edit_button_frame=Frame(self.user_profile_child2_frame,bg="#1B1A55")
        self.edit_button_frame.grid(row=4,pady=30)

        self.edit_button=Button(self.edit_button_frame,text="Edit Profile",font=("Roboto",15),bg="#535C91",fg="white",width=10,height=1,cursor="hand2",command=lambda: self.edit_profile(self.root, self.controller))
        self.edit_button.pack(expand=True)

        self.back_button_frame=Frame(self.user_profile_child2_frame,bg="white")
        self.back_button_frame.grid(row=5,column=0,pady=(0,10))

        self.back_button=Button(self.back_button_frame,text="Back",font=("Roboto",15),bg="white",fg="black",width=10,height=1,cursor="hand2", command=self.switch_to_home_page) #####
        self.back_button.pack(expand=True)

    def switch_to_home_page(self):
        self.controller.show_home_page()

    def edit_profile(self,root,controller):
        #self.controller.show_frame(Register)
        print("Edit Profile")
        self.controller=controller
        self.root=root

        self.popup = Toplevel(root)
        self.popup.attributes('-topmost', 'true')
        self.popup.title("Edit Profile")
        self.popup.geometry("800x630")
        self.popup.configure(bg="#070F2B")

        self.popup_frame=Frame(self.popup,bg="#070F2B")
        self.popup_frame.pack(fill=BOTH,expand=True)

        self.first_name_frame=Frame(self.popup_frame,bg="#1B1A55",height=50,width=700)
        self.first_name_frame.pack(pady=(60,0))

        self.label_first_name=Label(self.first_name_frame,text="First Name :",font=("Roboto",18),bg="#535C91",fg="#D8C4B6")
        self.label_first_name.grid(row=0,column=0,padx=(5,5),pady=5)

        self.entry_first_name_updated=Entry(self.first_name_frame,font=("Roboto",16),width=30)
        #self.entry_first_name_updated.insert(0, self.controller.user.first_name)
        self.entry_first_name_updated.insert(0, self.first_name)
        self.entry_first_name_updated.grid(row=0, column=1, padx=(5, 10), pady=5)


        self.last_name_frame=Frame(self.popup_frame,bg="#1B1A55",height=50,width=700)
        self.last_name_frame.pack(pady=(36,0))

        self.label_last_name=Label(self.last_name_frame,text="Last Name :",font=("Roboto",18),bg="#535C91",fg="#D8C4B6")
        self.label_last_name.grid(row=0,column=0,padx=(5,5),pady=5)

        self.entry_last_name_updated=Entry(self.last_name_frame,font=("Roboto",16),width=30)
        self.entry_last_name_updated.insert(0, self.last_name)
        self.entry_last_name_updated.grid(row=0, column=1, padx=(5, 10), pady=5)


        self.username_frame=Frame(self.popup_frame,bg="#1B1A55",height=50,width=700)
        self.username_frame.pack(pady=(36,0))

        self.label_username=Label(self.username_frame,text="Username :",font=("Roboto",18),bg="#535C91",fg="#D8C4B6")
        self.label_username.grid(row=0,column=0,padx=(5,5),pady=5)

        self.entry_username_updated=Entry(self.username_frame,font=("Roboto",16),width=30)
        self.entry_username_updated.insert(0, self.user_name)
        self.entry_username_updated.grid(row=0, column=1, padx=(5, 10), pady=5)


        self.password_frame=Frame(self.popup_frame,bg="#1B1A55",height=50,width=700)
        self.password_frame.pack(pady=(36,0))

        self.label_password=Label(self.password_frame,text="Password :",font=("Roboto",18),bg="#535C91",fg="#D8C4B6")
        self.label_password.grid(row=0,column=0,padx=(5,5),pady=5)

        self.entry_password_updated=Entry(self.password_frame,font=("Roboto",16),width=30)
        self.entry_password_updated.insert(0, self.controller.user.password)
        self.entry_password_updated.grid(row=0, column=1, padx=(5, 10), pady=5)


        self.profile_photos_frame=Frame(self.popup_frame,bg="#1B1A55",height=50,width=700)
        self.profile_photos_frame.pack(pady=(36,0))

        self.label_choose_small_photo=Label(self.profile_photos_frame, text="Profile Photo for Home:", font=("Roboto",18),bg="#535C91",fg="#D8C4B6")
        self.label_choose_small_photo.grid(row=0,column=0,padx=(5,5),pady=5)

        self.button_choose_small_photo=Button(self.profile_photos_frame,text="Choose a File",font=("Roboto",13),width=12,height=1,cursor="hand2",command=lambda:self.on_small_img_button_click())
        self.button_choose_small_photo.grid(row=0,column=1,padx=(5,5),pady=5)

        self.label_choose_big_photo=Label(self.profile_photos_frame, text="Profile Photo:", font=("Roboto",18),bg="#535C91",fg="#D8C4B6")
        self.label_choose_big_photo.grid(row=0,column=2,padx=(30,5),pady=5) #

        self.button_choose_big_photo=Button(self.profile_photos_frame,text="Choose a File",font=("Roboto",13),width=12,height=1,cursor="hand2",command=lambda: self.on_big_img_button_click())
        self.button_choose_big_photo.grid(row=0,column=3,padx=(5,5),pady=5)


        self.save_changes_frame=Frame(self.popup_frame,bg="#1B1A55",height=40,width=700)
        self.save_changes_frame.pack(pady=(45,0)) #

        self.button_save_changes=Button(self.save_changes_frame,text="Save Changes",font=("Roboto",16),bg="#1B1A55",fg="#D8C4B6",width=15,height=1,cursor="hand2",command=lambda: self.save_user_changes())
        self.button_save_changes.pack(expand=True)
    
    def save_user_changes(self):
        user_change=User(first_name=self.entry_first_name_updated.get(),last_name=self.entry_last_name_updated.get(),user_name=self.entry_username_updated.get(),password=self.entry_password_updated.get(),big_image_path=self.big_img_path,small_image_path=self.small_img_path,id=self.controller.user.id)
        self.user_service=self.controller.main_service.user_service
        self.updated_user=self.user_service.update_user(user_change)
        self.controller.user=self.updated_user
        self.controller.show_user_profile()
        messagebox.showinfo("Info", "Successfully saved!")
        #self.apply_changes()
        

    
    def apply_changes(self):
        self.controller.user=self.updated_user
        self.label_first_name_get.config(text=self.updated_user.first_name)
        self.label_last_name_get.config(text=self.updated_user.last_name)
        self.label_username_get.config(text=self.updated_user.user_name)
        self.entry_first_name_updated.delete(0,END)
        self.entry_last_name_updated.delete(0,END)
        self.entry_username_updated.delete(0,END)
        self.entry_password_updated.delete(0,END)
        self.popup.destroy()


    def on_small_img_button_click(self):
        self.small_img_path=self.save_file()

    def on_big_img_button_click(self):
        self.big_img_path=self.save_file()

    def save_file(self):
        file=filedialog.askopenfile(filetypes=[("Profile Photo Files", ".png")])
        if file is None:
            return
        file_path="medias/images/pp/"+file.name.split("/")[-1]
        try:
            shutil.copy(file.name,file_path)
        except:
            pass
        return file_path


    def __del__(self):
        self.popup.destroy()
