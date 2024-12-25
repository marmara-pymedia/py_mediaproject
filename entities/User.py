from entities.Media import Media
import json

class User:
    def __init__(self,first_name,last_name,user_name,password,favourite_medias=None,image_location="default",id=-1):
        self.id=id
        self.first_name=first_name
        self.last_name=last_name
        self.user_name=user_name
        self.password=password
        self.favourite_medias=favourite_medias if favourite_medias is not None else []
        self.image_location=image_location

    def toJSON(self):
        return json.dumps(
            self, default=lambda o: o.__dict__,
            sort_keys=False, indent=4
        )
