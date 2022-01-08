from abc import ABC,abstractmethod

class CartServiceInterface(ABC):
    def addItemtoCart(self,Item):
        pass
    def removeItem(self,cart,Item):
        pass
    def updateItemCount(self,cart,Item,Count):
        pass
    def checkout(self,cart):
        pass
    def getItemList(self,cart):
        pass
