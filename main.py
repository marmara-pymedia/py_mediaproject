
from homePage import HomePage
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

    def show_frame(self,frame_class):
        new_frame=frame_class(self.root,self)
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame=new_frame
        self.current_frame.pack(fill=BOTH,expand=True)


def main():
    root=Tk()
    mainApp=MainApp(root)
    root.mainloop()



main()
#test
