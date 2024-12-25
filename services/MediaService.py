import json
from entities.Media import Media
from entities.Media import *

class MediaService:
    def __init__(self):
        pass

    def add_media(self,media:Media):
        medias=self.get_all()
        media.id=medias[-1].id+1 if len(medias)!=0 else 1
        medias.append(media)
        with open("data/medias.json","w") as file:
            file.write(json.dumps([json.loads(media.toJSON()) for media in medias]))

    def get_media_by_id(self,id:int):
        medias=self.get_all()
        for media in medias:
            if media.id==id:
                return media
        return None
    
    def get_media_by_category(self,category:Category):
        medias=self.get_all()
        for media in medias:
            if media.category.id==category.id:
                return media
        return None
    def get_all(self)->list[Media]:
        with open("data/medias.json","r") as file:
            medias=json.load(file)
        new_medias=[]
        for media in medias:
            new_media=Media(**media)
            new_medias.append(new_media.toObject())
        return new_medias
    
    def update_media(self,media:Media):
        medias=self.get_all()
        for i in medias:
            if(i.id==media.id):
                i.category=media.category
                i.description=media.description
                i.bg_image_path=media.bg_image_path
                i.cover_image_path=media.cover_image_path
                i.note=media.note
                i.score=media.score
                i.title=media.title
                i.type=media.type
                i.watch_state=media.watch_state        
        with open("data/medias.json","w") as file:
            file.write(json.dumps([media.__dict__ for media in medias]))
    
    def delete_media(self,media:Media):
        medias=self.get_all()
        for i in medias:
            if(i.id==media.id):
                medias.remove(i)
                break
            
        with open("data/medias.json","w") as file:
            file.write(json.dumps([media.__dict__ for media in medias]))

    