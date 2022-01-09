from models.User import User

class Seller(User):
    def __init__(self,name,phone):
        super().__init__(name,phone)
        self.ProductList = []