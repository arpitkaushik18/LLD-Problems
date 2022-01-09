from models.Theater import Theater
from services.theater_service_interface import TheaterServiceInterface

class TheaterService(TheaterServiceInterface):
    TheaterList = {}
    def addTheater(self,name,location,limit):
        theater = Theater(name,location,limit)
        theater.set_id()

        self.__class__.TheaterList[theater.get_id()] = theater
        return theater
