from models.User import User
from models.Cart import Cart

class Customer(User):
    def __init__(self,name,phone):
        super().__init__(name,phone)
        self.cart = Cart()
        self.orderHistory = []

