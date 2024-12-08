from login import Login
from tkinter import *

def main():
    root=Tk()
    root.title("Pyflix")
    root.geometry("1920x1080")

    Login(root)

    root.mainloop()

main()