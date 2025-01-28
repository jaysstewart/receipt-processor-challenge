from src.model.item import Item
import uuid


class Receipt:
    def __init__(self, retailer: str, purchaseDate: str, purchaseTime: str, items: list[Item], total: str):
        self.id = uuid.uuid4()
        self.retailer = retailer
        self.purchaseDate = purchaseDate
        self.purchaseTime = purchaseTime
        self.items = items
        self.total = total
        self.points = None
