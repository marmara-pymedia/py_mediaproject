from tkinter import *
from tkinter import font
from tkinter import ttk
from components.mediaCover import MediaCover

class HomePage:
    def __init__(self,root):
        self.root=root


        self.home_frame=Frame(self.root, bg="#070F2B")
        self.home_frame.pack(expand=True,fill=BOTH)
    #Navi
        self.navi_frame=Frame(self.home_frame,bg="#1B1A55",height=50)
        self.navi_frame.pack(side=TOP,fill=X,pady=29)

        self.searchbar_frame=Frame(self.navi_frame,bg="#1B1A55",width=285,height=50)
        self.searchbar_frame.grid(row=0,column=0,padx=(1478,40))
        self.searchbar_entry=Entry(self.searchbar_frame,font=("Roboto",16))
        self.searchbar_entry.place(width=220,height=40,y=5,x=5)
        self.searchbar_img = PhotoImage(file="medias/icons/searchbar.png")
        self.searchbar_button=Button(self.searchbar_frame,image=self.searchbar_img)
        self.searchbar_button.img_reference=self.searchbar_img
        self.searchbar_button.place(height=50,width=50,x=230)

        self.profile_frame=Frame(self.navi_frame,bg="#1B1A55",width=50,height=50)
        self.profile_frame.grid(row=0,column=1)
        self.profile_img=PhotoImage(file="medias/icons/profileIcon.png")
<<<<<<< Updated upstream
        self.profile_img_label=Label(self.profile_frame,image=self.profile_img,bg="pink")
        self.profile_img_label.img_reference=self.profile_img
        self.profile_img_label.pack()
=======
        self.profile_img_button=Button(self.profile_frame,image=self.profile_img,bg="#1B1A55",bd=0)
        self.profile_img_button.img_reference=self.profile_img
        self.profile_img_button.pack()

>>>>>>> Stashed changes
    #/Navi
    #Body
        self.main_body_frame=Frame(self.home_frame, bg="#070F2B")
        self.main_body_frame.pack(expand=True,fill=BOTH)

        self.body_canvas=Canvas(self.main_body_frame)
        self.body_canvas.pack(side=LEFT,fill=BOTH,expand=True,padx=(160,160))

        self.body_scrollbar=ttk.Scrollbar(self.main_body_frame,orient=VERTICAL,command=self.body_canvas.yview)
        self.body_scrollbar.pack(side=RIGHT,fill=Y)

        self.body_canvas.configure(yscrollcommand=self.body_scrollbar)
        self.body_canvas.bind("<Configure>",lambda e:self.body_canvas.configure(scrollregion=self.body_canvas.bbox("all")))

        self.body_frame=Frame(self.body_canvas,bg="#070F2B")

        self.body_canvas.create_window((0,0),window=self.body_frame,anchor="nw")
        #Favourites
        self.favourites_frame=Frame(self.body_frame,bg="#1B1A55")
        self.favourites_frame.pack(side=TOP,pady=(40,0),padx=(80,80),fill=X)
        self.favourites_container=Frame(self.favourites_frame,bg="#1B1A55")
        self.favourites_container.pack(padx=(30,0),pady=(20,20))
        for i in range(5):
            MediaCover(self.favourites_container).get_frame().grid(row=0,column=i,padx=(0,30))
        #/Favourites
        #Medias
        self.medias_frame=Frame(self.body_frame,bg="#1B1A55")
        self.medias_frame.pack(side=LEFT,padx=80,pady=(50,0))
        self.medias_container=Frame(self.medias_frame,bg="#1B1A55")
        self.medias_container.pack(padx=(30,0),pady=(20,20))
        for i in range(5):
            for j in range(3):
                MediaCover(self.medias_container).get_frame().grid(row=i,column=j,padx=(0,30),pady=(0,30))
        #/Medias
    #/Body
            

        






