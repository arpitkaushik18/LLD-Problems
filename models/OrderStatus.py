import enum

class OrderStatus(enum):
    CREATED = 0
    PENDING = 1
    UNSHIPPED = 2
    SHIPPED = 3
    CANCELLED = 4
    COMPLETED = 5