from utils.Utils import get_unique_sequence

class Theater:
    def __init__(self,name,location,capacity):
        self.location = location
        self.capacity = capacity
        self.name = name

        self.ListofShows = []
    def set_id(self):
        self.id = get_unique_sequence()

    def get_id(self):
        return self.id

    def getSeats(self):
        return self.capacity
