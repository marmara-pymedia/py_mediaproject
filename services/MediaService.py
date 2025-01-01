import json
from entities.Media import Media
from entities.Category import Category
from entities.Type import Type
from entities.WatchState import WatchState

class MediaService:
    def __init__(self,category_service,type_service,usermedia_service):
        self.category_service=category_service
        self.type_service=type_service
        self.usermedia_service=usermedia_service
        
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
    
    def get_all_media_by_categories(self,categories:list[Category]):
        medias=self.get_all()
        filtered_medias=[]
        for media in medias:
            if any(media.category.id == c.id for c in categories):
                filtered_medias.append(media)
        return filtered_medias
    
    def get_media_by_type(self,type:Type):
        medias=self.get_all()
        for media in medias:
            if media.type.id==type.id:
                return media
        return None
    
    def get_all_media_by_types(self,types:list[Type]):
        medias=self.get_all()
        filtered_medias=[]
        for media in medias:
            if any(media.type.id == t.id for t in types):
                filtered_medias.append(media)
        return filtered_medias
    
    
    def get_media_by_score(self,score:int):
        medias=self.get_all()
        for media in medias:
            if media.score==score:
                return media
        return None
    
    def get_all_media_by_scores(self,user_id:int,scores:list[int]):
        medias=self.get_all()
        filtered_medias=[]
        print(self.usermedia_service)
        for media in medias:
            usermedia=self.usermedia_service.get_usermedia_by_user_id_and_media_id(user_id,media.id)
            if(usermedia is not None and any(usermedia.score == s for s in scores)):
                print(media.title)
                filtered_medias.append(media)
        return filtered_medias
    
    
    def get_media_by_watch_state(self,watch_state:WatchState):
        medias=self.get_all()
        for media in medias:
            if media.watch_state.id==watch_state.id:
                return media
        return None
    
    def get_all_media_by_watch_states(self,user_id,watch_states:list[WatchState]):
        medias=self.get_all()
        filtered_medias=[]
        for media in medias:
            usermedia=self.usermedia_service.get_usermedia_by_user_id_and_media_id(user_id,media.id)
            if(usermedia is not None and any(usermedia.watch_state.id == w.id for w in watch_states)):
                filtered_medias.append(media)
        return filtered_medias
    
    def get_filtered_medias(self,*media_lists:list[Media])->list[Media]:
        filtered_media_list=media_lists[0]
        for media_list in media_lists:
            filtered_media_list=[media for media in filtered_media_list if any(media.id == m.id for m in media_list)]
        return filtered_media_list


    def get_all(self)->list[Media]:
        with open("data/medias.json","r") as file:
            medias=json.load(file)
        new_medias=[]
        for media in medias:
            new_media=Media(media["title"],media["description"],self.type_service.get_by_id(media["type_id"]),self.category_service.get_by_id(media["category_id"]),media["cover_image_path"],media["bg_image_path"],media["id"])
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
                i.title=media.title
                i.type=media.type     
        
        for media in medias:
            if(media.id==media.id):
                medias.remove(media)
                break
        medias.append(media)
        with open("data/medias.json","w") as file:
            file.write(json.dumps([json.loads(media.toJSON()) for media in medias]))
    
    def delete_media(self,media:Media):
        medias=self.get_all()
        for i in medias:
            if(i.id==media.id):
                medias.remove(i)
                break
            
        with open("data/medias.json","w") as file:
            file.write(json.dumps([json.loads(media.toJSON()) for media in medias]))

    