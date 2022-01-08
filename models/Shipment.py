from utils.Utils import numberCounter

class Shipment:
    def __init__(self):
        self.shipmentNumber = numberCounter()
        self.date = None
        self.estimateArrival = None
        self.orderDetails = None