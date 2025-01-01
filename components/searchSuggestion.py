from tkinter import *
from tkinter import ttk

class SearchSuggestion:
    def __init__(self,root:Frame,controller,media):
        self.root=root
        self.media=media
        self.controller=controller
        self.suggestion_frame=Frame(self.root,width=220,height=100,cursor="hand2")
        self.suggestion_frame.bind("<Button-1>", self.on_suggestion_click)
        
        self.suggestion_content_frame=Frame(self.suggestion_frame,width=220,height=50)
        self.suggestion_content_frame.bind("<Button-1>", self.on_suggestion_click)
        self.suggestion_content_frame.grid_propagate(0)
        self.suggestion_content_frame.grid(row=0)

        self.content_title_label=Label(self.suggestion_content_frame,text=media.title)
        self.content_title_label.bind("<Button-1>", self.on_suggestion_click)
        self.content_title_label.grid(row=0,column=0,padx=(5,0),pady=(5,0),sticky=W)

        self.content_type_label=Label(self.suggestion_content_frame,text=media.type.name)
        self.content_type_label.bind("<Button-1>", self.on_suggestion_click)
        self.content_type_label.grid(row=1,column=0,padx=(5,150),sticky=W)

        self.content_score_label=Label(self.suggestion_content_frame,text=controller.main_service.usermedia_service.get_usermedia_by_user_id_and_media_id(controller.user.id,media.id).score if controller.main_service.usermedia_service.get_usermedia_by_user_id_and_media_id(controller.user.id,media.id) is not None else "-")
        self.content_score_label.bind("<Button-1>", self.on_suggestion_click)
        self.content_score_label.grid(row=1,column=1,sticky=W,padx=(0,5))

        
    def on_suggestion_click(self,event):
        self.controller.show_media_detail_page(self.media)

    
    def getFrame(self):
        return self.suggestion_frame



