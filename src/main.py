from fastapi import FastAPI

from src.model.item import Item
from src.model.receipt import Receipt
from src.points import Points
import uvicorn

app = FastAPI()

points = Points()

@app.get("/")
async def test():
    receipt = Receipt("Walmart", "2021-10-10", "12:00",
                      [Item("apple", "1.00"), Item("banana", "2.00")], "3.00")
    return {"message": Points.alphanumericCharactersRule(points, receipt)}

if __name__ == '__main__':
    uvicorn.run(app, port=8000)
