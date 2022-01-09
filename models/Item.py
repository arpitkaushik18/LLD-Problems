from models.Product import Product

class Item():
    def __init__(self,Product,count):
        self.productID = Product.get_id()
        self.count = count
        self.price = Product.get_price()*count

    def get_price(self):
        return self.price