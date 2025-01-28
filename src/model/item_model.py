from pydantic import BaseModel


class ItemModel(BaseModel):
    price: str
    shortDescription: str
