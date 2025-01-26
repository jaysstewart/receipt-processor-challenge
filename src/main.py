from fastapi import FastAPI

from src.model.item import Item
from src.model.receipt import Receipt
from src.points import Points
import uvicorn

app = FastAPI()

points = Points()

@app.get("/")
async def test():
    # receipt = Receipt("Target", "2022-01-01", "13:01",
    #                   [Item("Mountain Dew 12PK", "6.49"), Item("Emils Cheese Pizza", "12.25"),
    #                    Item("Knorr Creamy Chicken", "1.26"), Item("Doritos Nacho Cheese", "3.35"), Item("   Klarbrunn 12-PK 12 FL OZ  ", "12.00")],
    #                   "35.35")

    receipt = Receipt("M&M Corner Market", "2022-03-20", "14:33", [Item("Gatorade", "2.25"),
                                                                   Item("Gatorade", "2.25"), Item("Gatorade", "2.25"), Item("Gatorade", "2.25")], "9.00")
    return {"message": Points.calculatePoints(points, receipt)}

@app.post("/receipts/process")
async def process_receipt(receipt: Receipt):


if __name__ == '__main__':
    uvicorn.run(app, port=8000)
