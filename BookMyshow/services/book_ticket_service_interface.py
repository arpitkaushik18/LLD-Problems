from abc import ABC,abstractmethod

class BookTicketInterface:
    @abstractmethod
    def book_ticket(self,show,user,seats):
        pass