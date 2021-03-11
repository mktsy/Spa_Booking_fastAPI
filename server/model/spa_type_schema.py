from typing import Optional
from pydantic import BaseModel, Field


class MineralSchema(BaseModel):
    id: str = Field(...)
    type: str = Field(...)
    price: float = Field(...)
    time: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "id": "Blist001",
                "type": "The spa offers hot springs and mineral springs.",
                "price": "1000-1500 baht"
            }
        }


class UpdateSpaModel(BaseModel):
    type: Optional[str]
    description: Optional[str]
    price: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "type": "Mineral Spring Spa",
                "description": "The spa offers hot springs and mineral springs.",
                "price": "1500-2000 baht"
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