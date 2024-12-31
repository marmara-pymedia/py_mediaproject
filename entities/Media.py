from entities.Category import Category
from entities.Type import Type
from entities.WatchState import WatchState
import json

class Media:
    def __init__(self,title,description,type:Type,category:Category,cover_image_path="default",bg_image_path="default",id=-1):
        self.title=title
        self.description=description
        self.type=type
        self.category=category
        self.cover_image_path=cover_image_path
        self.bg_image_path=bg_image_path
        self.id=id
        pass

    def toJSON(self):
        return json.dumps(
            self, default=lambda o: o.__dict__,
            sort_keys=False, indent=4
        )
    
    def toObject(self):
        media_dict = self.__dict__
        self.category = Category(**media_dict["category"])
        self.type = Type(**media_dict["type"])
        return self