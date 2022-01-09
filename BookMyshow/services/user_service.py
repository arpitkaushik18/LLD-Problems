from models.GuestUser import GuestUser
from models.RegisteredUser import ResgisteredUser

from services.user_service_interface import UserServiceInterface

class UserService(UserServiceInterface):
    GuestUserDetails = {}
    RegisteredUserDetails = {}
    def addGuestUser(self,name):
        guestuser = GuestUser(name)
        guestuser.set_id()

        self.__class__.GuestUserDetails[guestuser.get_id()] = guestuser
        return guestuser

    def addRegisteredUser(self,name):
        registereduser = ResgisteredUser(name)
        registereduser.set_id()

        self.__class__.RegisteredUserDetails[registereduser.get_id()] = registereduser
        return registereduser

