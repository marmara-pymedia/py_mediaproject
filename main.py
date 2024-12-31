
from homePage import HomePage
from MediaDetailPage import mediaDetail
from tkinter import *
from userProfile import UserProfile
from services.UserService import UserService
from entities.User import User

class MainApp():
    def __init__(self,root):
        self.root=root
        root.title("Pyflix")
        root.geometry("1920x1080")
        root.configure(bg="#070F2B")
        self.current_frame=None
        self.user:User=None
        self.user=UserService().get_user_by_id(1)
        self.show_frame(HomePage)

    def show_frame(self,frame_class,*args):
        new_frame=frame_class(self.root,self,*args)
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame=new_frame
        self.current_frame.pack(fill=BOTH,expand=True)

    def show_user_profile(self):
        self.show_frame(UserProfile)
    def show_home_page(self):
        self.show_frame(HomePage)
    def show_media_detail_page(self,media):
        self.show_frame(mediaDetail,media)


    def refresh_frame(self):
        self.show_frame(self.current_frame.__class__)


def main():
    root=Tk()
    mainApp=MainApp(root)
    root.mainloop()



main()
#test
