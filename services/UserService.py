import json
from entities.User import *
from entities.User import User
# from services.MediaService import MediaService

class UserService:
    def __init__(self,media_service) -> None:
        self.media_service=media_service
        pass

    def add_user(self,user:User):
        users=self.get_all()
        user.id=users[-1].id+1 if len(users)!=0 else 1
        users.append(user)
        with open("data/users.json","w") as file:
            file.write(json.dumps([json.loads(user.toJSON()) for user in users]))

    def get_user_by_id(self,id:int):
        users=self.get_all()
        for user in users:
            if user.id==id:
                return user
        return None
    
    def get_all(self):
        with open("data/users.json","r") as file:
            users=json.load(file)
        new_users=[]
        for user in users:
            new_user=User(user["first_name"],user["last_name"],user["user_name"],user["password"],[self.media_service.get_media_by_id(id) for id in user["favourite_medias_id_list"]],user["big_image_path"],user["small_image_path"],user["id"])
            new_users.append(new_user.toObject())
        return new_users
    
    def update_user(self,user:User):
        users=self.get_all()
        for i in users:
            if(i.id==user.id):
                i.first_name=user.first_name
                i.last_name=user.last_name
                i.big_image_path=user.big_image_path
                i.small_image_path=user.small_image_path
                i.password=user.password
                i.favourite_medias=user.favourite_medias
                i.user_name=user.user_name
        self.delete_user(user)
        self.add_user(user)
        return user
    
    def delete_user(self,user:User):
        users=self.get_all()
        for i in users:
            if(i.id==user.id):
                users.remove(i)
                break
            
        with open("data/users.json","w") as file:
            file.write(json.dumps([json.loads(user.toJSON()) for user in users]))
    
    def add_favourite_media(self,user:User,media:Media):
        users=self.get_all()
        for i in users:
            if(i.id==user.id):
                i.favourite_medias.append(media)
                break
        
        with open("data/users.json","w") as file:
            file.write(json.dumps([json.loads(user.toJSON()) for user in users]))



