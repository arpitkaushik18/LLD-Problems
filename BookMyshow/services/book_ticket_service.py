from services.book_ticket_service_interface import BookTicketInterface
from models.Ticket import Ticket
from models.User import User

class BookTicketService(BookTicketInterface):
    def book_ticket(self,show,user,seats):
        availableSeats = show.Theater.getSeats()

        if(availableSeats > 0 and availableSeats>=seats):
            show.Theater.capacity-= seats
            ticket = Ticket(user.name,show.ShowTime,seats,show)
            print("Succesfull Booked for "+ user.name)
            user.bookingHistory.append(ticket)
            return ticket
        else:
            print("Sold Out")