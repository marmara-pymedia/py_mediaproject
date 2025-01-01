from tkinter import *
from tkinter import PhotoImage
import textwrap
from entities.Usermedia import Usermedia
from components.MovieUpdate import MovieUpdate


class mediaDetail(Frame):
    def __init__(self,root,controller,media):
        Frame.__init__(self,root)
        self.media=media
        self.controller=controller
        self.root=root
        print("Media Detail")
        self.root.title("Media Detail Page")
        
        self.mediaService = self.controller.main_service.media_service
        self.usermediaService = self.controller.main_service.usermedia_service
        self.watch_state_service = self.controller.main_service.watch_state_service
        if self.usermediaService.get_usermedia_by_user_id_and_media_id(self.controller.user.id,self.media.id) is None:
            self.usermediaService.add_usermedia(Usermedia(user=self.controller.user,watch_state=self.watch_state_service.get_by_id(1),score=0,note="",media=self.media))
        self.usermedia=self.usermediaService.get_usermedia_by_user_id_and_media_id(self.controller.user.id,self.media.id)
        self.user=self.controller.user
        self.update_form=None
        

        # BG FRAME
        self.bgFrame=Frame(self, bg="#070F2B", height=1080, width=1920)
        self.bgFrame.pack_propagate(0)
        self.bgFrame.pack(fill=BOTH, expand=True)

        # MEDIA BACKGROUND
        self.movie=PhotoImage(file=self.media.bg_image_path)
        self.mediaLabel=Label(self.bgFrame,image=self.movie, borderwidth=0, highlightthickness=0)
        self.mediaLabel.img_reference=self.movie
        self.mediaLabel.pack(fill=BOTH,expand=True , pady=(150))  
        # will delete upper part, ones json is connected DELETE        

         # Bottom-left Frame
        self.bottomLeftFrame = Frame(self.mediaLabel,bg="#535C91")
        self.bottomLeftFrame.pack(padx=(43), pady=(409,7),side=LEFT)

        # TITLE
        self.wrapped_title = textwrap.fill(self.media.title,width=20)
        self.title_label = Label(self.bottomLeftFrame, text=self.wrapped_title, font=("Roboto",40,"bold"),fg="White",background="#535C91")
        self.title_label.grid(row=0, sticky="W")

        # DESCRIPTION
        self.wrapped_description = textwrap.fill(self.media.description, width=50)  # Adjust width as needed
        self.description_label = Label(self.bottomLeftFrame, text=self.wrapped_description, font=("Roboto",12),fg="White",background="#535C91")
        self.description_label.grid(row=1, sticky="W")

        # TYPE
        self.type_frame = Frame(self.bottomLeftFrame)
        self.type_frame.grid(row=2, sticky="W")
        
        self.type_text = Label(self.type_frame, text="Type : ", font=("Roboto", 20 , "bold"), fg="white",background="#535C91")
        self.type_text.grid(row=0,column=0)
        self.type_data = Label(self.type_frame, text=self.media.type.name, font=("Roboto", 20), fg="white",background="#535C91")
        self.type_data.grid(row=0,column=1)

        # CATEGORY
        self.category_frame = Frame(self.bottomLeftFrame, bg="lightyellow")
        self.category_frame.grid(row=3, sticky="W")
        
        self.category_text = Label(self.category_frame, text="Category : ", font=("Roboto", 20 , "bold") , fg="white",background="#535C91")
        self.category_text.grid(row=0,column=0)
        self.category_data = Label(self.category_frame, text=self.media.category.name, font=("Roboto", 20), fg="white",background="#535C91")
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


        # Note UPDTAED BEFOREHAND



        # SCORE UPDTAED BEFOREHAND

        if self.usermedia.score == 1:
            self.rating=self.star_1
            
        elif self.usermedia.score == 2:
            self.rating=self.star_2
                        
        elif self.usermedia.score == 3:
            self.rating=self.star_3

        elif self.usermedia.score == 4:
            self.rating=self.star_4

        elif self.usermedia.score == 5:
            self.rating=self.star_5
        

        # EDIT - BUTTON
        self.editButtonFrame=Frame(self.bottomRightFrame, width="80", height="80")
        self.editButtonFrame.grid(row=0,column=0,padx=(10),pady=(10))
        self.edit_button=Button(self.editButtonFrame,image=self.edit, command=self.toggle_edit_options)
        self.edit_button.img_reference=self.edit
        self.edit_button.grid(row=0,column=0)
        
        # DELETE - BUTTON
        self.deleteButtonFrame=Frame(self.bottomRightFrame, width="80", height="80")
        self.deleteButtonFrame.grid(row=0,column=1, padx=(10),pady=(10))
        self.delete_button=Button(self.deleteButtonFrame, image=self.delete, command=self.toggle_delete_options)
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
        self.leavenote_button=Button(self.leavenoteButtonFrame, image=self.leavenote, command=self.toggle_note_frame)
        self.leavenote_button.img_reference=self.leavenote_button
        self.leavenote_button.grid(row=0,column=4)

        # WATCH-STATE UPDATED BEFOREHAND

        if self.usermedia.watch_state.id == 1:
            self.view_button.config(bg="#FB4141")
            

        elif self.usermedia.watch_state.id == 2:
            self.view_button.config(bg="#FFC145")
            
        elif self.usermedia.watch_state.id == 3:
            self.view_button.config(bg="#5CB338")


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


        #  -------------------------- FOR note -----------------------------------------------
        # NOTE FRAME (Initially hidden)
        self.noteFrame = Frame(self.mediaLabel, bg="#535C91")
        self.noteFrame.place_forget() # Hide initially

        # NOTE ENTRY
        self.note_text = Text(self.noteFrame, font=("Comic Sans MS",18,"bold"),fg="black",background="#d8c4b6", width=20, height=3)
        self.note_text.grid(row=0, column=0, padx=(10), pady=(10))

        # SUBMIT BUTTON
        self.submitIcon=PhotoImage(file="medias\icons\send.png")
        self.submit_button = Button(self.noteFrame, image=self.submitIcon, command=self.submit_note, bg="#3E7B27")
        self.submit_button.img_reference = self.submitIcon
        self.submit_button.grid(row=0, column=1, padx=(10), pady=(10))

        self.note_text.insert(END, self.usermedia.note)





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
        
        # DELETE TOGGLES

    def delete_media(self):
        self.usermediaService.delete_media(self.usermedia)
        

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
            self.media.watch_state = "not_watched"
            self.watch_state = self.watch_state_service.get_by_id(1)
    
        elif option == "watching":
            self.view_button.config(image=self.view, bg="#FFC145")
            self.media.watch_state = "watching"
            self.watch_state = self.watch_state_service.get_by_id(2)
        elif option == "watched":
            self.view_button.config(image=self.view, bg="#5CB338")
            self.media.watch_state = "watched"
            self.watch_state = self.watch_state_service.get_by_id(3)
        self.usermedia.watch_state = self.watch_state
        self.usermediaService.update(self.usermedia)




    # RATING OPTİON TOGGLES

    def select_rating_option(self, rating):
        self.selected_rating = rating
        self.ratingOptionsFrame.place_forget()  # Hide after selection 
        print(f"Selected rating: {rating} Stars")
        self.usermedia.score = rating
        self.usermediaService.update(self.usermedia)
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
            self.media.rating = 3

        elif rating == 4:
            self.rating_button.config(bg="white", image=self.star_4)
            self.rating_button.img_reference = self.star_4
            self.media.rating = 4
        elif rating == 5:
            self.rating_button.config(bg="white", image=self.star_5)
            self.rating_button.img_reference = self.star_5
            self.media.rating = 5


    def toggle_rating_options(self):
        if self.ratingOptionsFrame.winfo_y() != 100:
            self.ratingOptionsFrame.place(x=1585, y=100)
        else:
            self.ratingOptionsFrame.place_forget()


        # LEAVE note TOGGLES

    def toggle_note_frame(self):
        if self.noteFrame.winfo_y() != 300:
            self.noteFrame.place(x=1200, y=300)  # Adjust the position as needed
        else:
            self.noteFrame.place_forget()  # Hide initially

    def submit_note(self):
        self.note = self.note_text.get("1.0", END).strip()
        print(f"Note submitted: {self.note}")
        self.usermedia.note = self.note
        self.usermediaService.update(self.usermedia)
        self.noteFrame.place_forget()  # Hide the frame after submission


    def toggle_edit_options(self):
        if(self.update_form!=None):
            del self.update_form
        self.update_form=MovieUpdate(self,self.controller,self.media)
    
    def toggle_delete_options(self):
        self.mediaService.delete_media(self.media)
        self.usermediaService.delete_media(self.usermedia)
        self.controller.show_home_page()
        print("Media Deleted")
        self.destroy()
