from abc import ABC,abstractmethod

class UserServiceInterface(ABC):
    def addCustomer(self,name,phone):
        pass
    def addSeller(self,name,phone):
        pass
