from tkinter import *
from tkinter import ttk

class SearchSuggestion:
    def __init__(self,root:Frame,entry:Entry):
        self.root=root
        self.suggestion_frame=Frame(self.root,width=220,height=100,bg="black")
        
        self.suggestion_content_frame=Frame(self.suggestion_frame,width=220,height=50)
        self.suggestion_content_frame.grid_propagate(0)
        self.suggestion_content_frame.grid(row=0)
        self.content_title_label=Label(self.suggestion_content_frame,text="Film1")
        self.content_title_label.grid(row=0,column=0,padx=(5,0),pady=(5,0),sticky=W)
        self.content_type_label=Label(self.suggestion_content_frame,text="Film")
        self.content_type_label.grid(row=1,column=0,padx=(5,150),sticky=W)
        self.content_score_label=Label(self.suggestion_content_frame,text="4.5/5")
        self.content_score_label.grid(row=1,column=1,sticky=W,padx=(0,5))
        
    
    def getFrame(self):
        return self.suggestion_frame



