
from services.cart_service_interface import CartServiceInterface

class CartService(CartServiceInterface):

    def addItemtoCart(self,cart,item):
        cart.itemList.append(item)

    def removeItem(self,cart,Item):
        cart.itemList.remove(Item)

    def updateItemCount(self,cart,Item,Count):
        index = cart.itemList.index(Item)
        cart.itemList[index].count = Count

    def getItemList(self,cart):
        return cart.itemList

    def checkout(self,cart):
        cart.itemList.clear()

