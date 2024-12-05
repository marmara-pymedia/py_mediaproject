import json
from entities.User import User

class UserService:
    def __init__(self) -> None:
        pass

    def addUser(self,user:User):
        users=self.getAll()
        users.append(user)
        with open("data/users.json","w") as file:
            file.write(json.dumps([user.__dict__ for user in users]))

    def getUserById(self,id:int):
        users=self.getAll()
        for user in users:
            if user.id==id:
                return user
        return None
    
    def getAll():
        with open("data/users.json","r") as file:
            users=json.load(file)
        return [User(**user) for user in users]
    
    def updateUser(user:User):
        pass
    def deleteUser(user:User):
        pass



