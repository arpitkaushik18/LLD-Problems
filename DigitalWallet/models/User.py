from utils.utils import get_unique_sequence

class User(object):
    def __init__(self,name):
        self.name = name
        self.id = get_unique_sequence()

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name
