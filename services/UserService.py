import json
from entities.user import *
from entities.user import User

class UserService:
    def __init__(self) -> None:
        pass

    def addUser(self,user:User):
        users=self.getAll()
        user.id=users[-1].id+1 if len(users)!=0 else 1
        users.append(user)
        with open("data/users.json","w") as file:
            file.write(json.dumps([user.__dict__ for user in users]))

    def getUserById(self,id:int):
        users=self.getAll()
        for user in users:
            if user.id==id:
                return user
        return None
    
    def getAll(self):
        with open("data/users.json","r") as file:
            users=json.load(file)
        return [User(**user) for user in users]
    
    def updateUser(self,user:User):
        pass
    def deleteUser(self,user:User):
        pass



