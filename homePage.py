from tkinter import *
from tkinter import font
from tkinter import ttk
from components.mediaCover import MediaCover
from components.searchSuggestion import SearchSuggestion

class HomePage:
    def __init__(self,root):
        self.root=root

        self.home_frame=Frame(self.root,bg="#1B1A55")
        self.home_frame.pack(expand=True,fill=BOTH)
    #Navi
        self.navi_frame=Frame(self.home_frame,bg="#070F2B",height=200)
        self.navi_frame.pack(side=TOP,fill=X,pady=(0,20))

        self.searchbar_frame=Frame(self.navi_frame,bg="#070F2B",width=285,height=50)
        self.searchbar_frame.grid(row=0,column=0,padx=(1478,40),pady=10)

        sv=StringVar()
        sv.trace("w",lambda name,inedex,mode,sv=sv:onEntry(sv))
        self.searchbar_entry=Entry(self.searchbar_frame,font=("Roboto",16),textvariable=sv)

        self.searchbar_entry.place(width=220,height=40,y=5,x=5)
        self.searchbar_img = PhotoImage(file="medias/icons/searchbar.png")
        self.searchbar_button=Button(self.searchbar_frame,image=self.searchbar_img,bd=0)
        self.searchbar_button.img_reference=self.searchbar_img
        self.searchbar_button.place(height=50,width=50,x=230)

        self.profile_frame=Frame(self.navi_frame,bg="#9290C3",width=50,height=50)
        self.profile_frame.grid(row=0,column=1)
        self.profile_img=PhotoImage(file="medias/icons/profileIcon.png")
        self.profile_img_button=Button(self.profile_frame,image=self.profile_img,bg="#9290C3",bd=0)
        self.profile_img_button.img_reference=self.profile_img
        self.profile_img_button.pack()

    #/Navi
    
    #Body
        self.main_body_frame=Frame(self.home_frame,bg="#1B1A55")
        self.main_body_frame.pack(expand=True,fill=BOTH)

        self.body_canvas=Canvas(self.main_body_frame,bg="gray")
        self.body_canvas.pack(side=LEFT,fill=BOTH,expand=True,padx=(160,160))

        self.body_scrollbar=ttk.Scrollbar(self.main_body_frame,orient=VERTICAL,command=self.body_canvas.yview)
        self.body_scrollbar.pack(side=RIGHT,fill=Y)

        self.body_canvas.configure(yscrollcommand=self.body_scrollbar)
        self.body_canvas.bind("<Configure>",lambda e:self.body_canvas.configure(scrollregion=self.body_canvas.bbox("all")))

        self.body_frame=Frame(self.body_canvas,bg="#070F2B")

        self.body_canvas.create_window((0,0),window=self.body_frame,anchor="nw")
        #Favourites
        self.favourites_frame=Frame(self.body_frame,bg="#9290C3")
        self.favourites_frame.pack(side=TOP,pady=(80,0))
        self.favourites_container=Frame(self.favourites_frame,bg="#9290C3")
        self.favourites_container.pack()
        for i in range(5):
            if(i==0):
                MediaCover(self.favourites_container).get_frame().grid(row=0,column=i,padx=(15,15),pady=(15,15))
                continue
            MediaCover(self.favourites_container).get_frame().grid(row=0,column=i,padx=(0,15),pady=(15,15))
        #/Favourites

        #Filters
        self.filters_frame=Frame(self.body_frame,width=300,height=500)
        self.filters_frame.pack(side=RIGHT,padx=(0,80),pady=(50,0),anchor=NE)

        self.filters_title=Label(self.filters_frame,text="Filtreler",font=("Roboto",20))
        self.filters_title.grid(row=0,column=0,pady=(10,0))

        self.type_filter_frame=Frame(self.filters_frame,bg="gray")
        self.type_filter_frame.grid(row=1,column=0,padx=(20,20),pady=(20,0),sticky=W)
        self.type_filter_title=Label(self.type_filter_frame,text="Tür",font=("Roboto",16))
        self.type_filter_title.grid(row=0,column=0,sticky=W)
        self.type_filter_checkbox_frame=Frame(self.type_filter_frame)
        self.type_filter_checkbox_frame.grid(row=1,column=0)
        self.type_filter_checkbox1=Checkbutton(self.type_filter_checkbox_frame,text="Film",font=("Roboto",12))
        self.type_filter_checkbox1.grid(row=1,column=0,padx=(0,10))
        self.type_filter_checkbox2=Checkbutton(self.type_filter_checkbox_frame,text="Dizi",font=("Roboto",12))
        self.type_filter_checkbox2.grid(row=1,column=1)

        self.category_filter_frame=Frame(self.filters_frame,bg="gray")
        self.category_filter_frame.grid(row=2,column=0,padx=(20,20),pady=(20,0),sticky=W)
        self.category_filter_title=Label(self.category_filter_frame,text="Kategori",font=("Roboto",16))
        self.category_filter_title.grid(row=0,column=0,sticky=W)
        self.category_filter_checkbox_frame=Frame(self.category_filter_frame)
        self.category_filter_checkbox_frame.grid(row=1,column=0)
        self.category_filter_checkbox1=Checkbutton(self.category_filter_checkbox_frame,text="Belgesel",font=("Roboto",12))
        self.category_filter_checkbox1.grid(row=1,column=0,sticky=W,padx=(0,10))
        self.category_filter_checkbox2=Checkbutton(self.category_filter_checkbox_frame,text="Bilim Kurgu",font=("Roboto",12))
        self.category_filter_checkbox2.grid(row=1,column=1,sticky=W)
        self.category_filter_checkbox2=Checkbutton(self.category_filter_checkbox_frame,text="Gerilim",font=("Roboto",12))
        self.category_filter_checkbox2.grid(row=2,column=0,sticky=W,padx=(0,10))        
        self.category_filter_checkbox2=Checkbutton(self.category_filter_checkbox_frame,text="Macera",font=("Roboto",12))
        self.category_filter_checkbox2.grid(row=2,column=1,sticky=W)

        self.statue_filter_frame=Frame(self.filters_frame,bg="gray")
        self.statue_filter_frame.grid(row=3,column=0,padx=(20,20),pady=(20,0),sticky=W)
        self.statue_filter_title=Label(self.statue_filter_frame,text="İzlenme Durumu",font=("Roboto",16))
        self.statue_filter_title.grid(row=0,column=0,sticky=W)
        self.statue_filter_checkbox_frame=Frame(self.statue_filter_frame)
        self.statue_filter_checkbox_frame.grid(row=1,column=0)
        self.statue_filter_checkbox1=Checkbutton(self.statue_filter_checkbox_frame,text="İzlendi",font=("Roboto",12))
        self.statue_filter_checkbox1.grid(row=1,column=0,padx=(0,10))
        self.statue_filter_checkbox2=Checkbutton(self.statue_filter_checkbox_frame,text="İzlenmedi",font=("Roboto",12))
        self.statue_filter_checkbox2.grid(row=1,column=1)

        self.score_filter_frame=Frame(self.filters_frame,bg="gray")
        self.score_filter_frame.grid(row=4,column=0,padx=(20,20),pady=(20,20),sticky=W)
        self.score_filter_title=Label(self.score_filter_frame,text="Puan Durumu",font=("Roboto",16))
        self.score_filter_title.grid(row=0,column=0,sticky=W)
        self.score_filter_checkbox_frame=Frame(self.score_filter_frame)
        self.score_filter_checkbox_frame.grid(row=1,column=0)
        self.score_filter_checkbox1=Checkbutton(self.score_filter_checkbox_frame,text="1",font=("Roboto",12))
        self.score_filter_checkbox1.grid(row=1,column=0,sticky=W,padx=(0,10))
        self.score_filter_checkbox2=Checkbutton(self.score_filter_checkbox_frame,text="2",font=("Roboto",12))
        self.score_filter_checkbox2.grid(row=1,column=1,sticky=W,padx=(0,10))
        self.score_filter_checkbox3=Checkbutton(self.score_filter_checkbox_frame,text="3",font=("Roboto",12))
        self.score_filter_checkbox3.grid(row=1,column=2,sticky=W,padx=(0,10))
        self.score_filter_checkbox4=Checkbutton(self.score_filter_checkbox_frame,text="4",font=("Roboto",12))
        self.score_filter_checkbox4.grid(row=1,column=3,sticky=W,padx=(0,10))
        self.score_filter_checkbox5=Checkbutton(self.score_filter_checkbox_frame,text="5",font=("Roboto",12))
        self.score_filter_checkbox5.grid(row=1,column=4,sticky=W)

        #/Filters

        #Medias
        self.medias_frame=Frame(self.body_frame,bg="gray")
        self.medias_frame.pack(side=LEFT,padx=80,pady=(50,0))
        self.medias_container=Frame(self.medias_frame,bg="#070F2B")
        self.medias_container.pack(padx=(0,0),pady=(0,0))
        for i in range(5):
            for j in range(4):
                if(j==3):
                    MediaCover(self.medias_container).get_frame().grid(row=i,column=j,padx=(0,0),pady=(0,15))
                    continue
                MediaCover(self.medias_container).get_frame().grid(row=i,column=j,padx=(0,15),pady=(0,15))
        #/Medias

        #AddButton
        self.add_button_frame=Frame(self.main_body_frame,width=90,height=90)
        self.add_button_frame.pack_propagate(0)
        self.add_button_frame.pack(side=RIGHT,anchor=SE)
        self.add_button_image=PhotoImage(file="medias/icons/addMediaIcon.png")
        self.add_button=Button(self.add_button_frame,image=self.add_button_image,bd=0)
        self.add_button.img_reference=self.add_button_image
        self.add_button.pack()
        #/AddButton
    #/Body
    #PopUp
        self.search_suggestion_container=Frame(self.home_frame)
        self.search_suggestion_container.place(y=75,x=1483)
        def onEntry(sv:StringVar):
            for i in self.search_suggestion_container.winfo_children():
                    i.destroy()
            contains=False
            for i in ["abc","ade","fgh"]:
                if(i.startswith(sv.get()) and sv.get()!=""):
                    SearchSuggestion(self.search_suggestion_container,i).getFrame().pack()
                    contains=True
            if(contains):
                self.search_suggestion_container.place(y=75,x=1483)
            else:
                self.search_suggestion_container.place_forget()
    #/PopUp

        






