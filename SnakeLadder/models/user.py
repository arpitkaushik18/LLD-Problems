from utils.utils import get_unique_id

class User:
    def __init__(self,name):
        self.name = name
        self.id = get_unique_id()

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def getId(self):
        return self.id