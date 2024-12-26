from tkinter import *
from tkinter import font
from tkinter import ttk
from services.MediaService import MediaService
from services.CategoryService import CategoryService
from userProfile import UserProfile
from components.mediaCover import MediaCover
from components.searchSuggestion import SearchSuggestion
from components.MovieAdd import MovieAdd

class HomePage(Frame):
    def __init__(self,root,controller):
        Frame.__init__(self,root)
        self.root=self
        self.controller=controller
        self.add_form=None
        self.media_service=MediaService()
        self.category_service=CategoryService()

        self.medias=self.media_service.get_all()

        self.home_frame=Frame(self.root,bg="#1B1A55")
        self.home_frame.pack(expand=True,fill=BOTH)
    #Navi
        self.navi_frame=Frame(self.home_frame,bg="#070F2B",height=200)
        self.navi_frame.pack(side=TOP,fill=X,pady=(0,0))

        self.searchbar_frame=Frame(self.navi_frame,bg="#070F2B",width=285,height=50)
        self.searchbar_frame.grid(row=0,column=0,padx=(1478,40),pady=10)

        sv=StringVar()
        sv.trace("w",lambda name,index,mode,sv=sv:onEntry(sv))
        self.searchbar_entry=Entry(self.searchbar_frame,font=("Roboto",16),textvariable=sv)

        self.searchbar_entry.place(width=220,height=40,y=5,x=5)
        # self.searchbar_img = PhotoImage(file="medias/icons/searchbar.png")
        # self.searchbar_button=Button(self.searchbar_frame,image=self.searchbar_img,bd=0)
        # self.searchbar_button.img_reference=self.searchbar_img
        # self.searchbar_button.place(height=50,width=50,x=230)

        self.profile_frame=Frame(self.navi_frame,bg="#070F2B",width=50,height=50)
        self.profile_frame.grid(row=0,column=1)
        self.profile_img=PhotoImage(file="medias/icons/user_vector.png")
        self.profile_button=Button(self.profile_frame,image=self.profile_img,bg="#070F2B",bd=0,activebackground="#070F2B",command=self.on_profile_button_click)
        self.profile_button.img_reference=self.profile_img
        self.profile_button.pack()

    #/Navi
    
    #Body
        self.main_body_frame=Frame(self.home_frame,bg="#1B1A55")
        self.main_body_frame.pack(expand=True,fill=BOTH)

        self.body_canvas=Canvas(self.main_body_frame,bg="#070F2B",bd=0, highlightthickness=0, relief='ridge')
        self.body_canvas.pack(side=LEFT,fill=BOTH,expand=True,padx=(160,70))

        self.body_scrollbar=Scrollbar(self.main_body_frame,orient=VERTICAL,command=self.body_canvas.yview)
        self.body_scrollbar.pack(side=RIGHT,fill=Y)

        self.body_canvas.configure(yscrollcommand=self.body_scrollbar.set)
        self.body_canvas.bind("<Configure>",lambda e:self.body_canvas.configure(scrollregion=self.body_canvas.bbox("all")))
        self.body_canvas.bind_all("<MouseWheel>",self.on_mousewheel)

        self.body_frame=Frame(self.body_canvas,bg="#1B1A55")

        self.body_canvas.create_window((0,0),window=self.body_frame,anchor="nw")

        self.body_child1_frame=Frame(self.body_frame,bg="#070F2B")
        self.body_child1_frame.pack(pady=(50,0))

        self.body_child_frame=Frame(self.body_child1_frame,bg="#070F2B")
        self.body_child_frame.pack(padx=117,pady=(50,0))
        #Favourites
        self.favourites_frame=Frame(self.body_child_frame,bg="#535C91")
        self.favourites_frame.pack(side=TOP)
        self.favourites_container=Frame(self.favourites_frame,bg="#535C91",width=1300,height=200)
        self.favourites_container.pack(padx=20,pady=20)

        start_index=0
        last_index=5 if len(self.controller.user.favourite_medias)>=5 else len(self.controller.user.favourite_medias)
        for i in range(start_index,last_index):
            if(i==5):
                MediaCover(self.favourites_container,self.controller.user.favourite_medias[i]).get_frame().grid(row=0,column=i,padx=(0,0),pady=(0,0))
                continue
            MediaCover(self.favourites_container,self.controller.user.favourite_medias[i]).get_frame().grid(row=0,column=i,padx=(0,15),pady=(0,0))

        for i in range(5-last_index):
            if(i==5):
                MediaCover(self.favourites_container).get_frame().grid(row=0,column=i+last_index,padx=(0,0),pady=(0,0))
                continue
            MediaCover(self.favourites_container).get_frame().grid(row=0,column=i+last_index,padx=(0,15),pady=(0,0))

        # for i in range(5):
        #     if(i==4):
        #         MediaCover(self.favourites_container).get_frame().grid(row=0,column=i,padx=(0,0),pady=(0,0))
        #         continue
        #     MediaCover(self.favourites_container).get_frame().grid(row=0,column=i,padx=(0,15),pady=(0,0))
        #/Favourites

        #Filters
        self.filters_frame=Frame(self.body_child_frame,width=300,height=500,bg="#535C91")
        self.filters_frame.pack(side=RIGHT,padx=(0,0),pady=(50,0),anchor=NE)

        self.filters_title=Label(self.filters_frame,text="Filtreler",font=("Roboto",20),bg="#535C91",fg="white")
        self.filters_title.grid(row=0,column=0,pady=(10,0))

        self.type_filter_frame=Frame(self.filters_frame,bg="#535C91")
        self.type_filter_frame.grid(row=1,column=0,padx=(20,20),pady=(20,0),sticky=W)
        self.type_filter_title=Label(self.type_filter_frame,text="Tür",font=("Roboto",16),bg="#535C91",fg="white")
        self.type_filter_title.grid(row=0,column=0,sticky=W)
        self.type_filter_checkbox_frame=Frame(self.type_filter_frame,bg="#535C91")
        self.type_filter_checkbox_frame.grid(row=1,column=0)

        self.film_choice_num=IntVar()
        self.type_filter_checkbox1=Checkbutton(self.type_filter_checkbox_frame,text="Film",font=("Roboto",12),bg="#535C91",fg="white",selectcolor="black",activebackground="#535C91",activeforeground="white",variable=self.film_choice_num)
        self.type_filter_checkbox1.grid(row=1,column=0,padx=(0,10))

        self.dizi_choice_num=IntVar()
        self.type_filter_checkbox2=Checkbutton(self.type_filter_checkbox_frame,text="Dizi",font=("Roboto",12),bg="#535C91",fg="white",selectcolor="black",activebackground="#535C91",activeforeground="white",variable=self.dizi_choice_num)
        self.type_filter_checkbox2.grid(row=1,column=1)

        self.category_filter_frame=Frame(self.filters_frame,bg="#535C91")
        self.category_filter_frame.grid(row=2,column=0,padx=(20,20),pady=(20,0),sticky=W)
        self.category_filter_title=Label(self.category_filter_frame,text="Kategori",font=("Roboto",16),bg="#535C91",fg="white")
        self.category_filter_title.grid(row=0,column=0,sticky=W)
        self.category_filter_checkbox_frame=Frame(self.category_filter_frame,bg="#535C91")
        self.category_filter_checkbox_frame.grid(row=1,column=0)
        
        self.category_vars={category:BooleanVar() for category in self.category_service.get_all()}

        category_row=0
        category_col=0
        for category,var in self.category_vars.items():
            if(category_col==2):
                category_row+=1
                category_col=0
            self.category_filter_checkbox1=Checkbutton(self.category_filter_checkbox_frame,
                                                       text=category.name,
                                                       variable=var,
                                                       command=self.filter_medias,
                                                       font=("Roboto",12),
                                                       bg="#535C91",
                                                       fg="white",
                                                       selectcolor="black",
                                                       activebackground="#535C91",
                                                       activeforeground="white")
            self.category_filter_checkbox1.grid(row=category_row,column=category_col,sticky=W,padx=(0,10))
            category_col+=1


        self.statue_filter_frame=Frame(self.filters_frame,bg="#535C91")
        self.statue_filter_frame.grid(row=3,column=0,padx=(20,20),pady=(20,0),sticky=W)
        self.statue_filter_title=Label(self.statue_filter_frame,text="İzlenme Durumu",font=("Roboto",16),bg="#535C91",fg="white")
        self.statue_filter_title.grid(row=0,column=0,sticky=W)
        self.statue_filter_checkbox_frame=Frame(self.statue_filter_frame,bg="#535C91")
        self.statue_filter_checkbox_frame.grid(row=1,column=0)
        self.statue_filter_checkbox1=Checkbutton(self.statue_filter_checkbox_frame,text="İzlendi",font=("Roboto",12),bg="#535C91",fg="white",selectcolor="black",activebackground="#535C91",activeforeground="white")
        self.statue_filter_checkbox1.grid(row=1,column=0,padx=(0,10))
        self.statue_filter_checkbox2=Checkbutton(self.statue_filter_checkbox_frame,text="İzlenmedi",font=("Roboto",12),bg="#535C91",fg="white",selectcolor="black",activebackground="#535C91",activeforeground="white")
        self.statue_filter_checkbox2.grid(row=1,column=1)

        self.score_filter_frame=Frame(self.filters_frame,bg="#535C91")
        self.score_filter_frame.grid(row=4,column=0,padx=(20,20),pady=(20,20),sticky=W)
        self.score_filter_title=Label(self.score_filter_frame,text="Puan Durumu",font=("Roboto",16),bg="#535C91",fg="white")
        self.score_filter_title.grid(row=0,column=0,sticky=W)
        self.score_filter_checkbox_frame=Frame(self.score_filter_frame,bg="#535C91")
        self.score_filter_checkbox_frame.grid(row=1,column=0)
        self.score_filter_checkbox1=Checkbutton(self.score_filter_checkbox_frame,text="1",font=("Roboto",12),bg="#535C91",fg="white",selectcolor="black",activebackground="#535C91",activeforeground="white")
        self.score_filter_checkbox1.grid(row=1,column=0,sticky=W,padx=(0,10))
        self.score_filter_checkbox2=Checkbutton(self.score_filter_checkbox_frame,text="2",font=("Roboto",12),bg="#535C91",fg="white",selectcolor="black",activebackground="#535C91",activeforeground="white")
        self.score_filter_checkbox2.grid(row=1,column=1,sticky=W,padx=(0,10))
        self.score_filter_checkbox3=Checkbutton(self.score_filter_checkbox_frame,text="3",font=("Roboto",12),bg="#535C91",fg="white",selectcolor="black",activebackground="#535C91",activeforeground="white")
        self.score_filter_checkbox3.grid(row=1,column=2,sticky=W,padx=(0,10))
        self.score_filter_checkbox4=Checkbutton(self.score_filter_checkbox_frame,text="4",font=("Roboto",12),bg="#535C91",fg="white",selectcolor="black",activebackground="#535C91",activeforeground="white")
        self.score_filter_checkbox4.grid(row=1,column=3,sticky=W,padx=(0,10))
        self.score_filter_checkbox5=Checkbutton(self.score_filter_checkbox_frame,text="5",font=("Roboto",12),bg="#535C91",fg="white",selectcolor="black",activebackground="#535C91",activeforeground="white")
        self.score_filter_checkbox5.grid(row=1,column=4,sticky=W)

        #/Filters

        #Medias
        self.medias_frame=None
        self.load_medias()
        #/Medias

        #AddButton
        self.add_button_frame=Frame(self.main_body_frame,width=90,height=90,bg="#1B1A55")
        self.add_button_frame.pack_propagate(0)
        self.add_button_frame.pack(side=RIGHT,anchor=SE,padx=(0,10))
        self.add_button_image=PhotoImage(file="medias/icons/addMediaIcon.png")
        self.add_button=Button(self.add_button_frame,image=self.add_button_image,bd=0,bg="#1B1A55",activebackground="#1B1A55",command=self.on_add_button_click)
        self.add_button.img_reference=self.add_button_image
        self.add_button.pack()
        #/AddButton
    #/Body
    #PopUp
        self.search_suggestion_container=Frame(self.home_frame)
        def onEntry(sv:StringVar):
            for i in self.search_suggestion_container.winfo_children():
                    i.destroy()
            contains=False
            for i in ["abc","ade","fgh"]:
                if(i.startswith(sv.get()) and sv.get()!=""):
                    SearchSuggestion(self.search_suggestion_container,i).getFrame().pack()
                    contains=True
            if(contains):
                self.search_suggestion_container.place(y=60,x=1483)
            else:
                self.search_suggestion_container.place_forget()
    #/PopUp

    def load_medias(self):
        if(self.medias_frame!=None):
            self.medias_frame.destroy()

        self.medias_frame=Frame(self.body_child_frame,bg="gray")
        self.medias_frame.pack(side=LEFT,padx=0,pady=(50,0))
        self.medias_container=Frame(self.medias_frame,bg="#070F2B",width=1000,height=1000)
        self.medias_container.pack(padx=(0,0),pady=(0,0))

        col=0
        row=0
        for media in self.medias:
            if(col==3):
                MediaCover(self.medias_container,media).get_frame().grid(row=row,column=col,padx=(0,0),pady=(0,15))
                col=0
                row+=1
                continue
            MediaCover(self.medias_container,media).get_frame().grid(row=row,column=col,padx=(0,15),pady=(0,15))
            col+=1

            #Empty Medias
            empty_medias_count=10-(len(self.media_service.get_all())) if len(self.media_service.get_all())<10 else 0
        for i in range(empty_medias_count):
            if(col==3):
                MediaCover(self.medias_container).get_frame().grid(row=row,column=col,padx=(0,0),pady=(0,15))
                col=0
                row+=1
                continue
            MediaCover(self.medias_container).get_frame().grid(row=row,column=col,padx=(0,15),pady=(0,15))
            col+=1
            #/Empty Medias
    
    def filter_medias(self):
        selected_categories=[category for category,var in self.category_vars.items() if var.get()]

        if(len(selected_categories)==0):
            self.medias=self.media_service.get_all()
            self.load_medias()
            return
        
        self.medias=[self.media_service.get_media_by_category(category) for category in selected_categories if self.media_service.get_media_by_category(category)!=None]
        self.load_medias()


    def on_mousewheel(self,event):
        self.body_canvas.yview_scroll(int(-1*(event.delta/120)),"units")

    def on_add_button_click(self):
        self.load_medias()
        if(self.add_form!=None):
            del self.add_form
        self.add_form=MovieAdd(self,self.controller)

    def on_profile_button_click(self):
        self.controller.show_frame(UserProfile)

        






