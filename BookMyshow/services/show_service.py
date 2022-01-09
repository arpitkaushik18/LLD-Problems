from models.Show import Show
from services.show_service_interface import ShowServiceInterface

class ShowService(ShowServiceInterface):
    ShowList = {}
    def addShow(self,date,movie,theater):
        show = Show(date,movie,theater)
        show.set_id()

        self.__class__.ShowList[show.get_id()] = show
        return show

    def searchShow(self,name):
        shows = []
        res=""
        for show in self.ShowList.values():
            res = ""
            if(show.Movie.name == name):
                res += str(show.get_id()) + " " + show.Movie.name + " " + show.ShowTime + " " + str(show.Theater.getSeats())
                shows.append(res)
        return shows


