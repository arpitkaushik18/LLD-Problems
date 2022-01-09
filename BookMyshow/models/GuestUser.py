from models.User import User

class GuestUser(User):
    def __init__(self,name):
        super(GuestUser, self).__init__(name)