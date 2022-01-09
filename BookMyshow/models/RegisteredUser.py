from models.User import User

class ResgisteredUser(User):
    def __init__(self,name):
        super(ResgisteredUser, self).__init__(name)
        self.bookingHistory = []