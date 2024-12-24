class User:
    def __init__(self,first_name,last_name,user_name,password,image_location="default",id=-1):
        self.id=id
        self.first_name=first_name
        self.last_name=last_name
        self.user_name=user_name
        self.password=password
        self.image_location=image_location
