# This schema will help users send HTTP requests with the proper shape to the API -- e.g., the type of data to send and how to send it.
from typing import Optional
from pydantic import BaseModel, EmailStr, Field
import bcrypt
import random
import string


letters = string.ascii_letters
passwd = ( ''.join(random.choice(letters) for i in range(10)) )
hashed = bcrypt.hashpw(passwd.encode('utf-8'), bcrypt.gensalt())


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
                "password": hashed,
                "user_type": "customer"
            }
        }

''
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
                "password": hashed,
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

# In the code above, we defined a Pydantic Schema called StudentSchema that represents how the student data will be stored in your MongoDB database.