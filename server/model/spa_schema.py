from typing import Optional
from pydantic import BaseModel, Field

class SpaSchema(BaseModel):
    type: str = Field(...)
    description: Optional[str] = None
    price: str
    period_time: Optional[str] = None
    status: str

    class Config:
        schema_extra = {
            "example": {
                "type": "Mineral Spring Spa",
                "description": "The spa offers hot springs and mineral springs.",
                "price": "1000-1500 baht",
                "period_time": "10:00-11:00 AM, 6:00-7:00 PM, 7:30-8:30 PM",
                "status": "Available"
            }
        }


class UpdateSpaModel(BaseModel):
    type: Optional[str]
    description: Optional[str]
    price: Optional[str]
    period_time: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "type": "Mineral Spring Spa",
                "description": "The spa offers hot springs and mineral springs.",
                "price": "1500-2000 baht",
                "period_time": "6:00-7:00 PM, 7:30-8:30 PM",
                "status": "Not available"
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