from abc import ABC,abstractmethod

class MovieServiceInterface(ABC):
    @abstractmethod
    def addMovie(self,name,Genre,Lang):
        pass