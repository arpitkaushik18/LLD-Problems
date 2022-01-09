from utils.Utils import get_unique_sequence

class User:
    def __init__(self,name):
        self.id = None
        self.name = name
    def set_id(self):
        self.id = get_unique_sequence()
    def get_id(self):
        return self.id
    def get_name(self):
        return self.name