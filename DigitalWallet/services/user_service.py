from models.User import User
from services.user_service_interface import UserServiceInterface

class UserService(UserServiceInterface):
    userDetails = {}
    def add_user(self,name):
        user = User(name)
        self.__class__.userDetails[user.id] = user
        return user


