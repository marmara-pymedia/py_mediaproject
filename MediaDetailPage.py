from tkinter import *
from tkinter import PhotoImage
class mediaDetail:
    def __init__(self,root):
        self.root=root
        print("Media Detail")


        self.bgFrame=Frame(self.root, bg="#070F2B")
        self.bgFrame.pack(fill=BOTH, expand=True)

        # MEDIA BACKGROUND
        self.cats=PhotoImage(file="medias\images\\backgrounds\cats_bg.png")
        self.mediaLabel=Label(self.bgFrame,image=self.cats)
        self.mediaLabel.img_reference=self.cats
        self.mediaLabel.pack(fill=BOTH, pady=(95))
        

         # Bottom-left Frame
        self.bottomLeftFrame = Frame(self.mediaLabel,bg="#535C91")
        self.bottomLeftFrame.pack(padx=(43), pady=(409,7),side=LEFT)

        # TITLE
        self.title_label = Label(self.bottomLeftFrame, text="Title", font=("Roboto",40,"bold"),fg="White",background="#535C91")
        self.title_label.grid(row=0, sticky="W")

        # DESCRIPTION
        self.description_label = Label(self.bottomLeftFrame, text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. ", font=("Roboto",12),fg="White",background="#535C91")
        self.description_label.grid(row=1, sticky="W")

        # TYPE
        self.type_frame = Frame(self.bottomLeftFrame, )
        self.type_frame.grid(row=2, sticky="W")
        
        self.type_text = Label(self.type_frame, text="Type : ", font=("Roboto", 20 , "bold"), fg="white",background="#535C91")
        self.type_text.grid(row=0,column=0)
        self.type_data = Label(self.type_frame, text="Type from User JSON", font=("Roboto", 20), fg="white",background="#535C91")
        self.type_data.grid(row=0,column=1)

        # CATEGORY
        self.category_frame = Frame(self.bottomLeftFrame, bg="lightyellow")
        self.category_frame.grid(row=3, sticky="W")
        
        self.category_text = Label(self.category_frame, text="Category : ", font=("Roboto", 20 , "bold") , fg="white",background="#535C91")
        self.category_text.grid(row=0,column=0)
        self.category_data = Label(self.category_frame, text="Category from User JSON", font=("Roboto", 20), fg="white",background="#535C91")
        self.category_data.grid(row=0,column=1)


        # BOTTOM_RİGHT_FRAME
        self.bottomRightFrame = Frame(self.mediaLabel, bg="#535C91")
        self.bottomRightFrame.pack(padx=(43,100), pady=(490,7),side=RIGHT)

        # DEFINING IMAGE PATHS
        self.edit=PhotoImage(file="medias\icons\pen.png")
        self.delete=PhotoImage(file="medias\icons\\trashbin.png")
        self.rating=PhotoImage(file="medias\icons\star.png")
        self.view=PhotoImage(file="medias\icons\eye.png")
        self.leavenote=PhotoImage(file="medias\icons\leavenote.png")
        

        # EDIT - BUTTON
        self.editButtonFrame=Frame(self.bottomRightFrame, width="80", height="80")
<<<<<<< Updated upstream
        self.editButtonFrame.grid(row=0,column=0)
        self.edit_button=Button(self.editButtonFrame, command=self.edit_media)
        self.edit_button.image=self.edit
=======
        self.editButtonFrame.grid(row=0,column=0,padx=(10),pady=(10))
        self.edit_button=Button(self.editButtonFrame, image=self.edit, command=self.edit_media,)
        self.edit_button.img_reference=self.edit
        self.edit_button.grid(row=0,column=0)
>>>>>>> Stashed changes
        
        # DELETE - BUTTON
        self.deleteButtonFrame=Frame(self.bottomRightFrame, width="80", height="80")
        self.deleteButtonFrame.grid(row=0,column=1, padx=(10),pady=(10))
        self.delete_button=Button(self.deleteButtonFrame, image=self.delete, command=self.delete_media)
        self.delete_button.img_reference=self.delete
        self.delete_button.grid(row=0,column=1)
        # RATE - BUTTON
        self.ratingButtonFrame=Frame(self.bottomRightFrame, width="80", height="80")
        self.ratingButtonFrame.grid(row=0,column=2,padx=(10),pady=(10))
        self.rating_button=Button(self.ratingButtonFrame, image=self.rating, command=self.rate_media)
        self.rating_button.img_reference=self.rating
        self.rating_button.grid(row=0,column=2)
        
        # VIEW - BUTTON
        self.viewButtonFrame=Frame(self.bottomRightFrame, width="80", height="80")
        self.viewButtonFrame.grid(row=0,column=3,padx=(10),pady=(10))
        self.view_button=Button(self.viewButtonFrame, image=self.view, command=self.view_media)
        self.view_button.img_reference=self.view
        self.view_button.grid(row=0,column=3)
        
        # LEAVE note - BUTTON
        self.leavenoteButtonFrame=Frame(self.bottomRightFrame, width="80", height="80")
        self.leavenoteButtonFrame.grid(row=0,column=4,padx=(10),pady=(10))
        self.leavenote_button=Button(self.leavenoteButtonFrame, image=self.leavenote, command=self.leave_note)
        self.leavenote_button.img_reference=self.delete
        self.leavenote_button.grid(row=0,column=4)








        # -------------------------- FOR VİEW -----------------------------------------------

        # VIEW FRAME

        self.viewFrame = Frame(self.mediaLabel, bg="#535C91")
        self.viewFrame.pack(padx=(10), pady=(5), fill=BOTH,)
        self.viewFrame.place(x = 1700, y = 300)  # Hide initially

        # VIEW OPTIONS FRAME
        self.viewOptionsFrame = Frame(self.viewFrame, bg="#535C91")
        self.viewOptionsFrame.grid(row=1, column=3, padx=(10), pady=(10))
        self.viewOptionsFrame.grid_remove()  # Hide initially

        # VIEW OPTIONS BUTTONS
        self.not_watched_button = Button(self.viewOptionsFrame, text="Not Watched", command=lambda: self.select_view_option("not_watched"))
        self.not_watched_button.grid(row=0, column=0, pady=(5))
        self.watching_button = Button(self.viewOptionsFrame, text="Watching", command=lambda: self.select_view_option("watching"))
        self.watching_button.grid(row=1, column=0, pady=(5))
        self.watched_button = Button(self.viewOptionsFrame, text="Watched", command=lambda: self.select_view_option("watched"))
        self.watched_button.grid(row=2, column=0, pady=(5))

        # Placeholder for the selected view option
        self.selected_view_option = "not_watched"

    def toggle_view_options(self):
        if self.viewOptionsFrame.winfo_ismapped():
            self.viewOptionsFrame.grid_remove()
        else:
            self.viewOptionsFrame.grid()

    def select_view_option(self, option):
        self.selected_view_option = option
        self.viewOptionsFrame.grid_remove()
        print(f"Selected view option: {option}")
        # Update the view button icon based on the selected option
        if option == "not_watched":
            self.view_button.config(image=self.view)
        elif option == "watching":
            self.view_button.config(image=self.view)
        elif option == "watched":
            self.view_button.config(image=self.view)

    def edit_media(self):
        print("Edit Media")

    def delete_media(self):
        print("Delete Media")

    def rate_media(self):
        print("Rate Media")

    def view_media(self):
        print("View Info")

    def leave_note(self):
        print("Leave Note")



root=Tk()
root.title("Media Detail Page")
root.geometry("1920x1080")
mediaDetail(root)
root.mainloop()