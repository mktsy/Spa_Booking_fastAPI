from typing import Optional
from pydantic import BaseModel, Field


class SpaBookingSchema(BaseModel):
    name: str = Field(...)
    type: str = Field(...)
    price: float = Field(...)
    time: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "John Chaorai",
                "type": "Mineral Spa",
                "price": 1200,
                "time": "10:00-11:00 AM"
            }
        }


class UpdateSpaBookingModel(BaseModel):
    id: Optional[str]
    type: Optional[str]
    price: Optional[float]
    time: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "name": "John Chaorai",
                "type": "Mineral Spa",
                "price": 1500,
                "time": "07:00-08:00 PM"
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}