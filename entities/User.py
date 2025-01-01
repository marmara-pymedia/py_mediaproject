from entities.Media import Media
import json

class User:
    def __init__(self,first_name,last_name,user_name,password,favourite_medias=None,big_image_path="medias/logos/profilePng.png",small_image_path="medias/icons/user_vector.png",id=-1):
        self.id=id
        self.first_name=first_name
        self.last_name=last_name
        self.user_name=user_name
        self.password=password
        self.favourite_medias=favourite_medias if favourite_medias is not None else []
        self.big_image_path=big_image_path
        self.small_image_path=small_image_path

    def toJSON(self):
        return json.dumps(UserJSON(self.first_name,self.last_name,self.user_name,self.password,[media.id for media in self.favourite_medias],self.big_image_path,self.small_image_path,self.id).__dict__)
        return json.dumps(
            self, default=lambda o: o.__dict__,
            sort_keys=False, indent=4
        )

    def toObject(self):
        # user_dict = self.__dict__
        # self.favourite_medias = [Media(**media).toObject() for media in user_dict["favourite_medias"]]
        return self
    
class UserJSON:
    def __init__(self,first_name,last_name,user_name,password,favourite_medias_id_list:list[int]=None,big_image_path="Default",small_image_path="Default",id=-1):
        self.id=id
        self.first_name=first_name
        self.last_name=last_name
        self.user_name=user_name
        self.password=password
        self.favourite_medias_id_list=favourite_medias_id_list if favourite_medias_id_list is not None else []
        self.big_image_path=big_image_path
        self.small_image_path=small_image_path