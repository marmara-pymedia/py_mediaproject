from login import Login
from tkinter import *

def main():
    root=Tk()
    root.title("Pyflix")
    root.geometry("800x600")

    Login(root)

    root.mainloop()

main()