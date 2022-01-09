from utils.Utils import get_unique_sequence

class Movie:
    def __init__(self,name,genre,lang):
        self.id = None
        self.name = name
        self.rating = None

        self.language = lang
        self.Genre = genre

    def set_id(self):
        self.id = get_unique_sequence()

    def get_id(self):
        return self.id


