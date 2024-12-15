from tkinter import *
from tkinter import PhotoImage
class mediaDetail:
    def __init__(self,root):
        self.root=root
        print("Media Detail")


        self.bgFrame=Frame(self.root)
        self.bgFrame.pack(fill=BOTH, expand=True)

        # MEDIA BACKGROUND
        self.cats=PhotoImage(file="medias\images\\backgrounds\cats_bg.png")
        self.mediaLabel=Label(self.bgFrame,image=self.cats)
        self.mediaLabel.img_reference=self.cats
        self.mediaLabel.pack(fill=BOTH, pady=(95))
<<<<<<< Updated upstream
=======
        
>>>>>>> Stashed changes

         # Bottom-left Frame
        self.bottomLeftFrame = Frame(self.mediaLabel, bg= "lightblue")
        self.bottomLeftFrame.pack(padx=(43), pady=(409,7),side=LEFT)

        # TITLE
        self.title_label = Label(self.bottomLeftFrame, text="Title", font=("Roboto",40,"bold"),bg="lightgreen")
        self.title_label.grid(row=0, sticky="W")

<<<<<<< Updated upstream
        self.title_label = Label(self.bottomLeftFrame, text="Title", font=("Roboto",40,"bold"),bg="lightgreen").grid(row=0,column=0)

        self.description_label = Label(self.bottomLeftFrame, text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse sed dictum tellus, ac accumsan tortor. Curabitur vitae libero in massa lobortis dictum. Maecenas imperdiet ac enim vitae tempus. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vestibulum a est vel mi rutrum pulvinar.", font=("Roboto",30),bg="lightgreen").grid(row=1,column=0)


=======
        # DESCRIPTION
        self.description_label = Label(self.bottomLeftFrame, text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. ", font=("Roboto",12),bg="lightgreen")
        self.description_label.grid(row=1, sticky="W")

        # TYPE
        self.type_frame = Frame(self.bottomLeftFrame, bg="lightyellow")
        self.type_frame.grid(row=2, sticky="W")
        
        self.type_text = Label(self.type_frame, text="Type : ", font=("Roboto", 20 , "bold") , bg="lightgray", fg="white")
        self.type_text.grid(row=0,column=0)
        self.type_data = Label(self.type_frame, text="Type from User JSON", font=("Roboto", 20), bg="lime", fg="white")
        self.type_data.grid(row=0,column=1)
>>>>>>> Stashed changes

        # CATEGORY
        self.category_frame = Frame(self.bottomLeftFrame, bg="lightyellow")
        self.category_frame.grid(row=3, sticky="W")
        
        self.category_text = Label(self.category_frame, text="Category : ", font=("Roboto", 20 , "bold") , bg="lightgray", fg="white")
        self.category_text.grid(row=0,column=0)
        self.category_data = Label(self.category_frame, text="Category from User JSON", font=("Roboto", 20), bg="lime", fg="white")
        self.category_data.grid(row=0,column=1)


        # BOTTOM_RİGHT_FRAME
        self.bottomRightFrame = Frame(self.mediaLabel, bg="light blue")
        self.bottomRightFrame.pack(padx=(43,100), pady=(490,7),side=RIGHT)

        # DEFINING IMAGE PATHS
        self.edit=PhotoImage(file="medias\icons\pen.png")
        self.edit.img_reference=self.edit
        self.delete=PhotoImage(file="medias\icons\\trashbin.png")
        self.rating=PhotoImage(file="medias\icons\star.png")
        self.watch=PhotoImage(file="medias\icons\eye.png")
        self.note=PhotoImage(file="medias\icons\leavenote.png")
        

        # EDIT - BUTTON
        self.editButtonFrame=Frame(self.bottomRightFrame, width="80", height="80")
        self.editButtonFrame.grid(row=0,column=0)
        self.edit_button=Button(self.editButtonFrame, command=self.edit_media)
        self.edit_button.image=self.edit
        
        # DELETE - BUTTON
        self.editButtonFrame=Frame(self.bottomRightFrame, width="80", height="80")
        self.editButtonFrame.grid(row=0,column=1, padx=(20))
        self.edit_button=Button(self.editButtonFrame, image=self.edit, command=self.edit_media)

        # RATE - BUTTON
        self.editButtonFrame=Frame(self.bottomRightFrame, width="80", height="80")
        self.editButtonFrame.grid(row=0,column=2)
        self.edit_button=Button(self.editButtonFrame, image=self.edit, command=self.edit_media)
        
        # WATCHED - BUTTON
        self.editButtonFrame=Frame(self.bottomRightFrame, width="80", height="80")
        self.editButtonFrame.grid(row=0,column=3,padx=(20))
        self.edit_button=Button(self.editButtonFrame, image=self.edit, command=self.edit_media)
        
        # LEAVE note - BUTTON
        self.editButtonFrame=Frame(self.bottomRightFrame, width="80", height="80")
        self.editButtonFrame.grid(row=0,column=4)
        self.edit_button=Button(self.editButtonFrame, image=self.edit, command=self.edit_media)



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