from utils.Utils import numberCounter

class Order:
    def __init__(self):
        self.orderNumber = numberCounter()
        self.orderLogs = []
        self.orderStatus = None
        self.items = []
        self.amount = None
        self.shippingAddress = None
        
