from abc import ABC,abstractmethod

class UserServiceInterface(ABC):
    @abstractmethod
    def addGuestUser(self,name):
        pass
    def addRegisteredUser(self,name):
        pass
