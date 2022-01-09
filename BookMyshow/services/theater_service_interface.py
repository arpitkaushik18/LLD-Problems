from abc import ABC,abstractmethod

class TheaterServiceInterface(ABC):
    @abstractmethod
    def addTheater(self,name,location,limit):
        pass