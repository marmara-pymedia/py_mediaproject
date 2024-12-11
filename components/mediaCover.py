from tkinter import *

class MediaCover:
    def __init__(self,root):
        self.media_cover_frame=Frame(root,width=240,height=300,bg="black")
        self.media_cover_frame.pack_propagate(0)
        image_frame=Frame(self.media_cover_frame,bg="gray",width=240,height=240)
        image_frame.grid(row=0,padx=0,pady=(0,5))
        media_title_frame=Frame(self.media_cover_frame,bg="gray")
        media_title_frame.grid(row=1,padx=0,pady=(0,8))


    def get_frame(self):
        return self.media_cover_frame

root=Tk()
root.geometry("1920x1080")

MediaCover(root).get_frame().pack(expand=True)

root.mainloop()
