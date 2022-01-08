from utils.Utils import get_sequence

class Product:
    def __init__(self,name,description,pricr,cata,count):
        self.id = get_sequence()
        self.name = name
        self.description = description
        self.price = pricr
        self.ratings = None
        self.seller = None
        self.availableCount = count
        self.category = cata

    def set_seller(self,seller):
        self.seller = seller

    def set_quantity(self,quant):
        self.availableCount = quant