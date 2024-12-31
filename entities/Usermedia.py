from entities.WatchState import WatchState
from entities.User import User
from entities.Media import Media
import json

class Usermedia:
    def __init__(self, user:User, media:Media,watch_state:WatchState,score:int,note:str,id=-1):
        self.id = id
        self.user = user
        self.media = media
        self.watch_state = watch_state
        self.score = score
        self.note = note

    def toJSON(self):
        return json.dumps(
            self, default=lambda o: o.__dict__,
            sort_keys=False, indent=4
        )
    
    def toObject(self):
        usermedia_dict = self.__dict__
        self.user = User(**usermedia_dict["user"])
        self.media = Media(**usermedia_dict["media"])
        self.watch_state = WatchState(**usermedia_dict["watch_state"])
        return self
