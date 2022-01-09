from utils.Utils import get_unique_sequence
class Show:
    def __init__(self,date,movie,theater):
        self.id = None
        self.ShowTime = date
        self.availableSeats = None

        self.Movie = movie
        self.Theater = theater

    def getSeats(self):
        return self.availableSeats

    def set_id(self):
        self.id = get_unique_sequence()

    def get_id(self):
        return self.id