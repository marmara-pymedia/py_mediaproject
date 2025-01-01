from tkinter import *
from tkinter import ttk, filedialog
from tkinter import font
from tkinter import PhotoImage
from tkinter import messagebox
from entities.Type import Type
from entities.WatchState import WatchState
import shutil

from entities.Media import Media

#main için
#from components.movieAdd import MovieAdd

class MovieAdd:
    def __init__(self, root,controller) -> None:
        self.media_service=controller.main_service.media_service
        self.category_service=controller.main_service.category_service
        self.controller=controller
        self.root=root

        self.popup = Toplevel(root) #homepage olmalı
        self.popup.attributes('-topmost', 'true')
        self.popup.title("Add Movie")
        self.popup.geometry("800x630")
        self.popup.configure(bg="#070F2B")

        self.popup_frame=Frame(self.popup,bg="#070F2B")
        self.popup_frame.pack(fill=BOTH,expand=True)


        self.movie_name_frame=Frame(self.popup_frame,bg="#1B1A55",height=50,width=700)
        self.movie_name_frame.pack(pady=(60,0))

        self.label_movie_name=Label(self.movie_name_frame,text="Movie Name :",font=("Roboto",18),bg="#535C91",fg="#D8C4B6")
        self.label_movie_name.grid(row=0,column=0,padx=(5,5),pady=5)

        self.entry_movie_name=Entry(self.movie_name_frame,font=("Roboto",16),width=45)
        self.entry_movie_name.grid(row=0, column=1, padx=(5, 10), pady=5)


        self.movie_type_frame=Frame(self.popup_frame,bg="#1B1A55",height=50,width=700)
        self.movie_type_frame.pack(pady=(36,0))

        self.label_movie_type=Label(self.movie_type_frame,text="Movie Genre :",font=("Roboto",18),bg="#535C91",fg="#D8C4B6")
        self.label_movie_type.grid(row=0,column=0,padx=(5,5),pady=5)

        #movie type entry hali, combobox yerine kullanmak istersek diye
        #self.entry_movie_type=Entry(self.movie_type_frame,font=("Roboto",16),width=45)
        #self.entry_movie_type.grid(row=0, column=1, padx=(5, 10), pady=5)

        self.combo_movie_type=ttk.Combobox(self.movie_type_frame,font=("Roboto",15),width=45,values=[category.name for category in self.category_service.get_all()])
        self.combo_movie_type.grid(row=0, column=1, padx=10, pady=10)
        self.combo_movie_type.set("Choose a Genre")


        self.movie_files_frame=Frame(self.popup_frame,bg="#1B1A55",height=50,width=700)
        self.movie_files_frame.pack(pady=(36,0))

        self.label_choose_cover=Label(self.movie_files_frame, text="Cover:", font=("Roboto",18),bg="#535C91",fg="#D8C4B6")
        self.label_choose_cover.grid(row=0,column=0,padx=(5,5),pady=5)

        self.button_choose_cover=Button(self.movie_files_frame,text="Choose a File",font=("Roboto",13),width=12,height=1,cursor="hand2",command=lambda:self.on_cover_img_button_click())
        self.button_choose_cover.grid(row=0,column=1,padx=(5,5),pady=5)

        self.label_choose_bg=Label(self.movie_files_frame, text="Background:", font=("Roboto",18),bg="#535C91",fg="#D8C4B6")
        self.label_choose_bg.grid(row=0,column=2,padx=(60,5),pady=5)

        self.button_choose_bg=Button(self.movie_files_frame,text="Choose a File",font=("Roboto",13),width=12,height=1,cursor="hand2",command=lambda: self.on_bg_img_button_click())
        self.button_choose_bg.grid(row=0,column=3,padx=(5,5),pady=5)


        self.movie_description_frame=Frame(self.popup_frame,bg="#1B1A55",height=206,width=700)
        self.movie_description_frame.pack(pady=(36,0))

        self.label_movie_description=Label(self.movie_description_frame,text="Description :",font=("Roboto",18),bg="#535C91",fg="#D8C4B6")
        self.label_movie_description.grid(row=0,column=0,padx=(5,5),pady=5)

        self.text_movie_description=Text(self.movie_description_frame,width=68, height=15)
        self.text_movie_description.grid(row=0, column=1, padx=(5, 10), pady=(5,5))


        self.movie_save_frame=Frame(self.popup_frame,bg="#1B1A55",height=40,width=700)
        self.movie_save_frame.pack(pady=(20,0))

        self.button_save=Button(self.movie_save_frame,text="Save",font=("Roboto",16),bg="#1B1A55",fg="#D8C4B6",width=10,height=1,cursor="hand2",command=lambda: save_media())
        self.button_save.pack(expand=True)

        def save_media():
            media=Media(title=self.entry_movie_name.get(),description=self.text_movie_description.get("1.0", END).strip(),type=Type(1,"Film"),category=self.category_service.get_all()[self.combo_movie_type.current()],bg_image_path=self.bg_img_path,cover_image_path=self.cover_img_path)
            # print(media.__dict__)
            self.media_service.add_media(media)
            messagebox.showinfo("Info", "Successfully saved!")
            self.controller.refresh_frame()

    
    def on_cover_img_button_click(self):
        self.cover_img_path=self.save_file()

    def on_bg_img_button_click(self):
        self.bg_img_path=self.save_file()

    def save_file(self):
        file=filedialog.askopenfile(filetypes=[("Image Files", ".png")])
        if file is None:
            return
        file_path="medias/images/covers/"+file.name.split("/")[-1]
        try:
            shutil.copy(file.name,file_path)
        except:
            pass
        return file_path


    def __del__(self):
        self.popup.destroy()