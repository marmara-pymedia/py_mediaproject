import json

class User:
    def __init__(self,firstName,lastName,userName,password,imageLocation="default"):
        users=getAll()
        
        self.id=users[-1].id+1 if users.count!=0 else 1
        self.firstName=firstName
        self.lastName=lastName
        self.userName=userName
        self.password=password
        self.imageLocation=imageLocation

def getAll():
        with open("data/users.json","r") as file:
            users=json.load(file)
        return [User(**user) for user in users]