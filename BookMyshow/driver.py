from models.User import User
from models.Genre import Genre
from models.Language import Language

from services.user_service import UserService
from services.movie_service import MovieService
from services.show_service import ShowService
from services.theater_service import TheaterService
from services.book_ticket_service import BookTicketService

user1 = UserService()
user1 = user1.addRegisteredUser("Ayush")

user2 = UserService()
user2 = user2.addRegisteredUser("Piyush")

user3 = UserService()
user3 = user3.addGuestUser("Vimal")

movie1 = MovieService()
movie1 = movie1.addMovie("IronMan",Genre.ACTION,Language.English)

theater1 = TheaterService()
theater1 = theater1.addTheater("Big Cinema","Sector 137 Noida",40)

show1 = ShowService()
show1 = show1.addShow("1/1/21",movie1,theater1)

booking1 = BookTicketService()
booking1 = booking1.book_ticket(show1,user1,10)


searchResult = ShowService()
searchResultList = searchResult.searchShow("IronMan")
print(searchResultList)



