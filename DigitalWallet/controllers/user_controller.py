class UserController(object):
    def __init__(self,UserService):
        self.UserService = UserService

    def addUser(self, name):
        return self.UserService.add_user(name)