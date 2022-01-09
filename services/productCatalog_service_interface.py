from abc import ABC,abstractmethod

class ProductCatalogServiceInterface(ABC):
    def addCatagory(self, pcatalog,catagory):
        pass
    def updateSimilarProductsMap(self,cart,Item):
        pass
    def updateCategoryProductMap(self,cart,Item,Count):
        pass
    def updateProductSellerMap(self):
        pass
    def addProduct(self,cart):
        pass
    def searchProduct(self,cart):
        pass
    def searchCategory(self, cart):
        pass
    def updateProductQuantity(self, cart):
        pass
    def removeProduct(self, cart):
        pass
