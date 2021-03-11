from fastapi import APIRouter, Body, Depends
from fastapi.encoders import jsonable_encoder


from server.database.user_database import(
    add_user,
    update_user
)
from server.database.spa_database import(
    retrieve_spa,
    retrieve_spas,
)
from server.model.user_schema import(
    ErrorResponseModel,
    ResponseModel,
    UserSchema,
    UpdateUserModel,
    UserLoginSchema
)