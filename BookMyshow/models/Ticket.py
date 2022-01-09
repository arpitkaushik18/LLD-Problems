from utils.Utils import get_unique_sequence
class Ticket:
    def __init__(self,name,time,seats,show):
        self.id = None
        self.ownerName = name
        self.bookingTime = time
        self.noOfSeats = seats
        self.bookedShow = show

    def set_id(self):
        self.id = get_unique_sequence()

    def get_id(self):
        return self.id