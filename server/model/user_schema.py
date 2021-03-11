from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class UserSchema(BaseModel):
    name: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
    user_type: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "Pakpum Bunsong",
                "email": "makiin@gmail.com",
                "password": "1234",
                "user_type": "customer"
            }
        }


class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "lnwza007@gmail.com",
                "password": "weakpassword"
            }
        }

class UpdateUserModel(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    password: Optional[str]
    user_type: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "name": "Pakpum Bunsong",
                "email": "makiin@gmail.com",
                "password": "1234",
                "user_type": "customer"
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}