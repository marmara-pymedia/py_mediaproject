from services.UserService import UserService

class User:
    def __init__(self,firstName,lastName,userName,password,imageLocation="default"):
        userService=UserService()
        users=userService.getAll()
        
        self.id=users[-1].id+1 if users.count!=0 else 1
        self.firstName=firstName
        self.lastName=lastName
        self.userName=userName
        self.password=password
        self.imageLocation=imageLocation
