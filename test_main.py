from services.UserService import UserService
from entities.User import User
from entities.Media import Media
from services.MediaService import MediaService

userService=UserService()
mediaService=MediaService()

# userService.add_user(User("test","test","test","test"))
# print(userService.get_all())
# userService.add_favourite_media(userService.get_user_by_id(1),mediaService.get_media_by_id(1))
print(userService.get_user_by_id(1).favourite_medias[0].title)
