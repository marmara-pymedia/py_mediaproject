from tkinter import *
from tkinter import ttk

class MediaCover:
    def __init__(self,root):
        self.media_cover_frame_base=Frame(root,width=250,height=310,bg="black")
        self.media_cover_frame=Frame(self.media_cover_frame_base,width=240,height=300,bg="pink")
        self.media_cover_frame.pack(padx=(5,5),pady=(5,5))
        self.media_cover_frame.pack_propagate(0)
        self.media_cover_frame.grid_propagate(0)

        image_frame=Frame(self.media_cover_frame,bg="gray",width=250,height=240)
        image_frame.grid(sticky=W)
        media_image=PhotoImage(file="medias\images\cats cover.png")
        media_image_label=Label(image_frame,image=media_image)
        media_image_label.img_reference=media_image
        media_image_label.pack(fill=BOTH,expand=True)

        media_title_frame=Frame(self.media_cover_frame,bg="gray",width=250,height=20)
        media_title_frame.pack_propagate(0)
        media_title_frame.grid(row=1,column=0,padx=0,pady=(0,8))
        media_title=Label(media_title_frame,text="Süt İçen Kediler",font=("Roboto",9))
        media_title.pack(padx=12,anchor=W)

        media_extra_frame=Frame(self.media_cover_frame,bg="gray",width=250,height=20)
        media_extra_frame.grid_propagate(0)
        media_extra_frame.grid(row=2,column=0,padx=0,pady=(0,5))

        media_category_frame=Frame(media_extra_frame,height=20)
        media_category_frame.grid(row=0,column=0,padx=(6,8),sticky=W)
        media_category_title=Label(media_category_frame,text="Kategori:",font=("Roboto",8))
        media_category_title.grid(row=0,column=0,)
        media_category=Label(media_category_frame,text="Belgesel",font=("Roboto",8))
        media_category.grid(row=0,column=1)

        media_type_frame=Frame(media_extra_frame,height=20)
        media_type_frame.grid(row=0,column=1,padx=(0,8))
        media_type_title=Label(media_type_frame,text="Tür:",font=("Roboto",8))
        media_type_title.grid(row=0,column=0)
        media_type=Label(media_type_frame,text="Film",font=("Roboto",8))
        media_type.grid(row=0,column=1)

        media_score_frame=Frame(media_extra_frame,height=20,width=50)
        media_score_frame.grid(row=0,column=2)
        media_score_title=Label(media_score_frame,text="Score:",font=("Roboto",8))
        media_score_title.grid(row=0,column=0)
        media_score=Label(media_score_frame,text="4.5/5",font=("Roboto",8))
        media_score.grid(row=0,column=1)



    def get_frame(self):
        return self.media_cover_frame_base

# root=Tk()
# root.geometry("1920x1080")

# container=ttk.Frame(root,width=1920,height=1080)
# container.pack_propagate(False)
# canvas=Canvas(container)


# scroll_bar=ttk.Scrollbar(container,orient="vertical",command=canvas.yview)
# medias_frame=ttk.Frame(canvas)

# medias_frame.bind(
#     "<Configure>",
#     lambda e: canvas.configure(
#         scrollregion=canvas.bbox("all")
#     )
# )

# canvas.create_window((0, 0), window=medias_frame, anchor="nw")

# canvas.configure(yscrollcommand=scroll_bar.set)


# for i in range(5):
#     for j in range(5):
#         MediaCover(medias_frame).get_frame().grid(row=i,column=j,padx=1,pady=1)

# container.pack()
# canvas.pack(side="left",fill="both",expand=True)
# scroll_bar.pack(side="right",fill="y")

# root.mainloop()
