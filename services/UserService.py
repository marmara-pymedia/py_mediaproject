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
            file.write(json.dumps([user.__dict__ for user in users]))

    def get_user_by_id(self,id:int):
        users=self.get_all()
        for user in users:
            if user.id==id:
                return user
        return None
    
    def get_all(self):
        with open("data/users.json","r") as file:
            users=json.load(file)
        return [User(**user) for user in users]
    
    def update_user(self,user:User):
        users=self.get_all()
        for i in users:
            if(i.id==user.id):
                i.first_name=user.first_name
                i.last_name=user.last_name
                i.image_location=user.image_location
                i.password=user.password
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



