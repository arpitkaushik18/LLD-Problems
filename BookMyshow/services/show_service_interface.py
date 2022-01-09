from abc import ABC,abstractmethod

class ShowServiceInterface(ABC):
    @abstractmethod
    def addShow(self,date,movie,theater):
        pass
    def searchShow(self,name):
        pass