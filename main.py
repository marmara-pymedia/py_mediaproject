from login import Login
from register import Register
from homePage import HomePage
from tkinter import *
from userProfile import UserProfile


class MainApp():
    def __init__(self,root):
        self.root=root
        root.title("Pyflix")
        root.geometry("1920x1080")
        root.configure(bg="#070F2B")
        self.current_frame=None
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
