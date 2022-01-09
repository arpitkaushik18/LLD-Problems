from models.Customer import Customer
from models.Seller import Seller
from services.user_service_interface import UserServiceInterface

class UserService(UserServiceInterface):
    coustomerDetails = {}
    sellerDetails = {}
    def addCustomer(self,name,phone):
        customer = Customer(name,phone)

        self.__class__.coustomerDetails[customer.get_id()] = customer
        return customer

    def addSeller(self,name,phone):
        seller = Seller(name,phone)

        self.__class__.sellerDetails[seller.get_id()] = seller

        return seller
