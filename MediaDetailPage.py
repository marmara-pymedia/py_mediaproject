from tkinter import *
from tkinter import PhotoImage
class mediaDetail:
    def __init__(self,root):
        self.root=root


        print("Media Detail")

        self.bgFrame=Frame(self.root)
        self.bgFrame.pack(fill=BOTH, expand=True)

        self.cats=PhotoImage(file="medias\images\\backgrounds\cats_bg.png")
        self.mediaLabel=Label(self.bgFrame,image=self.cats)
        self.mediaLabel.img_reference=self.cats
        self.mediaLabel.pack(fill=BOTH)

         # Bottom-left Frame
        self.bottomLeftFrame = Frame(self.bgFrame, bg="lightgrey")
        self.bottomLeftFrame.pack(side=BOTTOM)

        # # Adding Details to the Bottom-left Frame
        # Label(self.bottomLeftFrame, text="Title:", font=("Arial", 10, "bold"), bg="lightgrey").grid(row=0, column=0, sticky=W, padx=5, pady=2)
        # self.titleLabel = Label(self.bottomLeftFrame, text="[Title from JSON]", font=("Arial", 10), bg="lightgrey")
        # self.titleLabel.grid(row=0, column=1, sticky=W, padx=5, pady=2)

        # Label(self.bottomLeftFrame, text="Media:", font=("Arial", 10, "bold"), bg="lightgrey").grid(row=1, column=0, sticky=W, padx=5, pady=2)
        # self.mediaLabel = Label(self.bottomLeftFrame, text="[Media from JSON]", font=("Arial", 10), bg="lightgrey")
        # self.mediaLabel.grid(row=1, column=1, sticky=W, padx=5, pady=2)

        # Label(self.bottomLeftFrame, text="Type:", font=("Arial", 10, "bold"), bg="lightgrey").grid(row=2, column=0, sticky=W, padx=5, pady=2)
        # self.typeLabel = Label(self.bottomLeftFrame, text="[Type from JSON]", font=("Arial", 10), bg="lightgrey")
        # self.typeLabel.grid(row=2, column=1, sticky=W, padx=5, pady=2)

        # Label(self.bottomLeftFrame, text="Category:", font=("Arial", 10, "bold"), bg="lightgrey").grid(row=3, column=0, sticky=W, padx=5, pady=2)
        # self.categoryLabel = Label(self.bottomLeftFrame, text="[Category from JSON]", font=("Arial", 10), bg="lightgrey")
        # self.categoryLabel.grid(row=3, column=1, sticky=W, padx=5, pady=2)

        # # Far-right Frame
        # self.rightFrame = Frame(self.bgFrame, bg="white", bd=2, relief=SOLID)
        # self.rightFrame.grid(row=0, column=2, rowspan=3, sticky=NE, padx=10, pady=10)

        # # Adding Buttons to the Far-right Frame
        # Button(self.rightFrame, text="Edit", font=("Arial", 10, "bold"), command=self.edit_media).grid(row=0, column=0, padx=5, pady=5, sticky=EW)
        # Button(self.rightFrame, text="Delete", font=("Arial", 10, "bold"), command=self.delete_media).grid(row=1, column=0, padx=5, pady=5, sticky=EW)
        # Button(self.rightFrame, text="Rating", font=("Arial", 10, "bold"), command=self.rate_media).grid(row=2, column=0, padx=5, pady=5, sticky=EW)
        # Button(self.rightFrame, text="View Info", font=("Arial", 10, "bold"), command=self.view_info).grid(row=3, column=0, padx=5, pady=5, sticky=EW)
        # Button(self.rightFrame, text="Leave Note", font=("Arial", 10, "bold"), command=self.leave_note).grid(row=4, column=0, padx=5, pady=5, sticky=EW)



    def edit_media(self):
        print("Edit Media")

    def delete_media(self):
        print("Delete Media")

    def rate_media(self):
        print("Rate Media")

    def view_info(self):
        print("View Info")

    def leave_note(self):
        print("Leave Note")



root=Tk()
root.title("Media Detail Page")
root.geometry("1920x1080")
mediaDetail(root)
root.mainloop()