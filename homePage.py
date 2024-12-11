from tkinter import *
from tkinter import font
from components.mediaCover import MediaCover

class HomePage:
    def __init__(self,root):
        self.root=root

        self.home_frame=Frame(self.root)
        self.home_frame.pack(expand=True,fill=BOTH)
    #Navi
        self.navi_frame=Frame(self.home_frame,bg="pink",height=50)
        self.navi_frame.pack(side=TOP,fill=X,pady=29)

        self.searchbar_frame=Frame(self.navi_frame,bg="pink",width=285,height=50)
        self.searchbar_frame.grid(row=0,column=0,padx=(1478,40))
        self.searchbar_entry=Entry(self.searchbar_frame,font=("Roboto",16))
        self.searchbar_entry.place(width=220,height=40,y=5,x=5)
        self.searchbar_img = PhotoImage(file="medias/icons/searchbar.png")
        self.searchbar_button=Button(self.searchbar_frame,image=self.searchbar_img)
        self.searchbar_button.img_reference=self.searchbar_img
        self.searchbar_button.place(height=50,width=50,x=230)

        self.profile_frame=Frame(self.navi_frame,bg="pink",width=50,height=50)
        self.profile_frame.grid(row=0,column=1)
        self.profile_img=PhotoImage(file="medias/icons/profileIcon.png")
        self.profile_img_label=Label(self.profile_frame,image=self.profile_img,bg="pink")
        self.profile_img_label.img_reference=self.profile_img
        self.profile_img_label.pack()
    #/Navi
    #Body
        self.body_frame=Frame(self.home_frame,bg="gray")
        self.body_frame.pack(side=TOP,fill=BOTH,pady=(55,0),padx=(160,160))
        #Favourites
        self.favourites_frame=Frame(self.body_frame,bg="pink")
        self.favourites_frame.pack(side=TOP,pady=(40,0),padx=(80,80),fill=X)
        self.favourites_container=Frame(self.favourites_frame,bg="pink")
        self.favourites_container.pack(padx=(30,0),pady=(20,20))
        for i in range(5):
            MediaCover(self.favourites_container).get_frame().grid(row=0,column=i,padx=(0,30))
        #/Favourites
        #Medias
        self.medias_frame=Frame(self.body_frame,bg="pink")
        self.medias_frame.pack(side=LEFT,padx=80,pady=(50,0))
        self.medias_container=Frame(self.medias_frame,bg="pink")
        self.medias_container.pack(padx=(30,0),pady=(20,20))
        for i in range(2):
            for j in range(3):
                MediaCover(self.medias_container).get_frame().grid(row=i,column=j,padx=(0,30),pady=(0,30))
        #/Medias
    #/Body
            

        






