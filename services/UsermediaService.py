from entities.Usermedia import Usermedia
import json

class UsermediaService:
    def __init__(self,user_service,media_service,watch_state_service):
        self.user_service=user_service
        self.media_service=media_service
        self.watch_state_service=watch_state_service

    def add_usermedia(self,usermedia:Usermedia):
        medias=self.get_all()
        usermedia.id=medias[-1].id+1 if len(medias)!=0 else 1
        medias.append(usermedia)
        with open("data/usermedias.json","w") as file:
            file.write(json.dumps([json.loads(media.toJSON()) for media in medias]))

    def get_media_by_id(self,id:int):
        medias=self.get_all()
        for media in medias:
            if media.id==id:
                return media
        return None
    
    def get_usermedias_by_user_id(self,user_id:int):
        medias=self.get_all()
        usermedias=[]
        for media in medias:
            if media.user.id==user_id:
                usermedias.append(media)
        return usermedias
    
    def get_usermedia_by_user_id_and_media_id(self,user_id:int,media_id:int):
        medias=self.get_all()
        for media in medias:
            print(media.user.id,media.media.id,user_id,media_id)
            if media.user.id==user_id and media.media.id==media_id:
                return media
        return None
    
    def get_all(self)->list[Usermedia]:
        with open("data/usermedias.json","r") as file:
            medias=json.load(file)
        new_medias=[]
        for media in medias:
            new_media=Usermedia(self.user_service.get_user_by_id(media["user_id"]),self.media_service.get_media_by_id(media["media_id"]),self.watch_state_service.get_by_id(media["watch_state_id"]),media["score"],media["note"],media["id"])
            new_medias.append(new_media.toObject())
        return new_medias