from typing import List

from pydantic import BaseModel

from src.model.item_model import ItemModel


class ReceiptModel(BaseModel):
    retailer: str
    purchaseDate: str
    purchaseTime: str
    items: List[ItemModel]
    total: str
