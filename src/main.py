import uuid
from fastapi import FastAPI, HTTPException
from src.model.receipt_model import ReceiptModel
from src.points import Points
import uvicorn

api = FastAPI()
pointsInstance = Points()


@api.get("/receipts/{request_id}/points")
async def get(request_id: uuid.UUID):
    response = Points.calculatePoints(pointsInstance, Points.read_receipt(pointsInstance, request_id))
    if response is None:
        raise HTTPException(status_code=404, detail="No receipt found for that ID.")

    return response


@api.post("/receipts/process")
async def post(request: ReceiptModel):
    response = pointsInstance.createReceipt(request)
    if response is None:
        raise HTTPException(status_code=422, detail="Invalid request.")
    return response


if __name__ == '__main__':
    uvicorn.run(api, port=8000)
