from login import Login
from register import Register
from tkinter import *

def main():
    root=Tk()
    root.title("Pyflix")
    root.geometry("1920x1080")

    Register(root)

    root.mainloop()

main()