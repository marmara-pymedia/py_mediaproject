import json

class User:
    def __init__(self,firstName,lastName,userName,password,imageLocation="default",id=-1):
        self.id=id
        self.firstName=firstName
        self.lastName=lastName
        self.userName=userName
        self.password=password
        self.imageLocation=imageLocation
