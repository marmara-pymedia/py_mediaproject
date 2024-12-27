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

        self.star_1=PhotoImage(file="medias\icons\star-1.png")
        self.star_2=PhotoImage(file="medias\icons\star-2.png")
        self.star_3=PhotoImage(file="medias\icons\star-3.png")
        self.star_4=PhotoImage(file="medias\icons\star-4.png")
        self.star_5=PhotoImage(file="medias\icons\star-5.png")
        

        # EDIT - BUTTON
        self.editButtonFrame=Frame(self.bottomRightFrame, width="80", height="80")
        self.editButtonFrame.grid(row=0,column=0)
        self.edit_button=Button(self.editButtonFrame, command=self.edit_media)
        self.edit_button.image=self.edit
        
        # DELETE - BUTTON
        self.deleteButtonFrame=Frame(self.bottomRightFrame, width="80", height="80")
        self.deleteButtonFrame.grid(row=0,column=1, padx=(10),pady=(10))
        self.delete_button=Button(self.deleteButtonFrame, image=self.delete, command=self.delete_media)
        self.delete_button.img_reference=self.delete
        self.delete_button.grid(row=0,column=1)
        # RATE - BUTTON
        self.ratingButtonFrame=Frame(self.bottomRightFrame, width="80", height="80")
        self.ratingButtonFrame.grid(row=0,column=2,padx=(10),pady=(10))
        self.rating_button=Button(self.ratingButtonFrame, image=self.rating, command=self.toggle_rating_options)
        self.rating_button.img_reference=self.rating
        self.rating_button.grid(row=0,column=2)
        
        # VIEW - BUTTON
        self.viewButtonFrame=Frame(self.bottomRightFrame, width="80", height="80")
        self.viewButtonFrame.grid(row=0,column=3,padx=(10),pady=(10))
        self.view_button=Button(self.viewButtonFrame, image=self.view, command=self.toggle_view_options)
        self.view_button.img_reference=self.view
        self.view_button.grid(row=0,column=3)
        
        # LEAVE note - BUTTON
        self.leavenoteButtonFrame=Frame(self.bottomRightFrame, width="80", height="80")
        self.leavenoteButtonFrame.grid(row=0,column=4,padx=(10),pady=(10))
        self.leavenote_button=Button(self.leavenoteButtonFrame, image=self.leavenote, command=self.leave_note)
        self.leavenote_button.img_reference=self.delete
        self.leavenote_button.grid(row=0,column=4)


        # -------------------------- FOR RATING -----------------------------------------------

          # RATING OPTIONS FRAME (Separate from bottomRightFrame)
        self.ratingOptionsFrame = Frame(self.mediaLabel, bg="#535C91")
        self.ratingOptionsFrame.place_forget()  # Hide initially

        # RATING OPTIONS BUTTONS

        self.one_star_button = Button(
            self.ratingOptionsFrame,
            image=self.star_1,
            command=lambda: self.select_rating_option(1),
            width=60,
            height=60
        )
        self.one_star_button.img_reference = self.star_1
        self.one_star_button.grid(row=0, column=0, pady=5, padx=5)

        self.two_star_button = Button(
            self.ratingOptionsFrame,
            image=self.star_2,
            command=lambda: self.select_rating_option(2),
            width=60,
            height=60
        )
        self.two_star_button.img_reference = self.star_2
        self.two_star_button.grid(row=1, column=0, pady=5, padx=5)

        self.three_star_button = Button(    
            self.ratingOptionsFrame,
            image=self.star_3,
            command=lambda: self.select_rating_option(3),
            width=60,
            height=60
        ) 
        self.three_star_button.img_reference = self.star_3
        self.three_star_button.grid(row=2, column=0, pady=5, padx=5)

        self.four_star_button = Button(
            self.ratingOptionsFrame,
            image=self.star_4,
            command=lambda: self.select_rating_option(4),
            width=60,
            height=60
        )
        self.four_star_button.img_reference = self.star_4
        self.four_star_button.grid(row=3, column=0, pady=5, padx=5)

        self.five_star_button = Button(
            self.ratingOptionsFrame,
            image=self.star_5,
            command=lambda: self.select_rating_option(5),
            width=60,
            height=60
        )
        self.five_star_button.img_reference = self.star_5
        self.five_star_button.grid(row=4, column=0, pady=5, padx=5)





        # -------------------------- FOR VİEW -----------------------------------------------

        # VIEW FRAME

        self.viewOptionsFrame = Frame(self.mediaLabel, bg="#535C91")
        self.viewOptionsFrame.place_forget()  # Hide initially

        # VIEW OPTIONS FRAME
        self.not_watched_button = Button(
            self.viewOptionsFrame,
            image=self.view,
            command=lambda: self.select_view_option("not_watched"),
            bg="#FB4141",
            width=60,
            height=60
        )
        self.not_watched_button.img_reference = self.view
        self.not_watched_button.grid(row=0, column=0, pady=5, padx=5)

        self.watching_button = Button(
            self.viewOptionsFrame,
            image=self.view,
            command=lambda: self.select_view_option("watching"),
            bg="#FFC145",
            width=60,
            height=60
        )
        self.watching_button.img_reference = self.view
        self.watching_button.grid(row=1, column=0, pady=5, padx=5)

        self.watched_button = Button(
            self.viewOptionsFrame,
            image=self.view,
            command=lambda: self.select_view_option("watched"),
            bg="#5CB338",
            width=60,
            height=60
        )
        self.watched_button.img_reference = self.view
        self.watched_button.grid(row=2, column=0, pady=5, padx=5)

        # Placeholder for the selected view option
        self.selected_view_option = "not_watched"

        # -------------------------- TOGGLES -----------------------------------------------
        
        # VIEW OPTİON TOGGLES

    def toggle_view_options(self):
        # Show or hide the view options
        if self.viewOptionsFrame.winfo_y() != 250:
            self.viewOptionsFrame.place(x = 1665, y = 250)  # Show if hidden
        else:
          self.viewOptionsFrame.place_forget()  # Hide initially

    def select_view_option(self, option):
        # Update the selected view option and icon
        self.selected_view_option = option
        self.viewOptionsFrame.place_forget()  # Hide after selection
        print(f"Selected view option: {option}")

        # Update the "View" button icon based on the selected option
        if option == "not_watched":
            self.view_button.config(image=self.view, bg="#FB4141")
        elif option == "watching":
            self.view_button.config(image=self.view, bg="#FFC145")
        elif option == "watched":
            self.view_button.config(image=self.view, bg="#5CB338")
    


    # RATING OPTİON TOGGLES

    def select_rating_option(self, rating):
        self.selected_rating = rating
        self.ratingOptionsFrame.place_forget()  # Hide after selection 
        print(f"Selected rating: {rating} Stars")
        # Update the rating button background color based on the selected rating
        self.rating_button.config(bg="#FFC145")

        if rating == 1:
            self.rating_button.config(bg="white", image=self.star_1)
            self.rating_button.img_reference = self.star_1
        elif rating == 2:
            self.rating_button.config(bg="white", image=self.star_2)
            self.rating_button.img_reference = self.star_2
        elif rating == 3:
            self.rating_button.config(bg="white", image=self.star_3)
            self.rating_button.img_reference = self.star_3
        elif rating == 4:
            self.rating_button.config(bg="white", image=self.star_4)
            self.rating_button.img_reference = self.star_4
        elif rating == 5:
            self.rating_button.config(bg="white", image=self.star_5)
            self.rating_button.img_reference = self.star_5

    def toggle_rating_options(self):
        if self.ratingOptionsFrame.winfo_y() != 100:
            self.ratingOptionsFrame.place(x=1585, y=100)
        else:
            self.ratingOptionsFrame.place_forget()

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