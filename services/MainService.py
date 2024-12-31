from services.UserService import UserService
from services.MediaService import MediaService
from services.UsermediaService import UsermediaService
from services.WatchStateService import WatchStateService
from services.CategoryService import CategoryService
from services.TypeService import TypeService

class MainService:
    def __init__(self):
        self.category_service=CategoryService()
        self.type_service=TypeService()
        self.media_service=MediaService(self.category_service,self.type_service,None)
        self.user_service=UserService(self.media_service)
        self.usermedia_service=UsermediaService(self.user_service,self.media_service,None)
        self.watch_state_service=WatchStateService()
        self.media_service.usermedia_service = self.usermedia_service
        self.usermedia_service.watch_state_service = self.watch_state_service