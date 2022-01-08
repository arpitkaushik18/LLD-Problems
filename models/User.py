from utils.Utils import get_sequence
class User:
    def __init__(self,name,phone):
        self.id = None
        self.name = None
        self.address = None
        self.phone = None
        self.username = None
        self.password = None

    def set_id(self):
        self.id = get_sequence()

    def get_id(self):
        return self.id

    