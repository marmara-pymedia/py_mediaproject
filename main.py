from login import Login
from register import Register
from homePage import HomePage
from tkinter import *
from userProfile import UserProfile

def main():
    root=Tk()
    root.title("Pyflix")
    root.geometry("1920x1080")

    HomePage(root)

    root.mainloop()

main()
#test
