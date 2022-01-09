from models.Movie import Movie
from services.movie_service_interface import MovieServiceInterface

class MovieService(MovieServiceInterface):
    MovieList = {}
    def addMovie(self,name,Genre,Lang):
        movie = Movie(name,Genre,Lang)
        movie.set_id()

        self.__class__.MovieList[movie.get_id()] = movie
        return movie
