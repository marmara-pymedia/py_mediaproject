import json
from entities.User import *
from entities.User import User

class UserService:
    def __init__(self) -> None:
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
            new_user=User(**user)
            new_users.append(new_user.toObject())
        return new_users
    
    def update_user(self,user:User):
        users=self.get_all()
        for i in users:
            if(i.id==user.id):
                i.first_name=user.first_name
                i.last_name=user.last_name
                i.image_location=user.image_location
                i.password=user.password
                i.favourite_medias=user.favourite_medias
                i.user_name=user.user_name
        
        with open("data/users.json","w") as file:
            file.write(json.dumps([user.__dict__ for user in users]))
    
    def delete_user(self,user:User):
        users=self.get_all()
        for i in users:
            if(i.id==user.id):
                users.remove(i)
                break
            
        with open("data/users.json","w") as file:
            file.write(json.dumps([user.__dict__ for user in users]))
    
    def add_favourite_media(self,user:User,media:Media):
        users=self.get_all()
        for i in users:
            if(i.id==user.id):
                i.favourite_medias.append(media)
                break
        
        with open("data/users.json","w") as file:
            file.write(json.dumps([json.loads(user.toJSON()) for user in users]))



