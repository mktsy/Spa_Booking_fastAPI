from fastapi import APIRouter, Body, Depends
from fastapi.encoders import jsonable_encoder
from server.auth.auth_handler import signJWT
from server.auth.auth_bearer import JWTBearer

from server.database.user_database import(
    update_user
)
from server.database.spa_database import(
    retrieve_spa,
    retrieve_spas,
    add_spa,
    update_spa,
    delete_spa
)
from server.database.spa_booking_database import(
    retrieve_spa_booking,
    retrieve_spas_booking,
    update_spa_booking,
    delete_spa_booking,
    add_spa_booking
)
from server.model.user_schema import (
    ErrorResponseModel,
    ResponseModel,
    OwnerLoginSchema,
    UpdateOwnerModel,
    OwnerSchema,
)
from server.model.spa_schema import(
    ErrorResponseModel,
    ResponseModel,
    SpaSchema,
    UpdateSpaModel
)
from server.model.spa_booking_schema import(
    ErrorResponseModel,
    ResponseModel,
    SpaBookingSchema,
    UpdateSpaBookingModel
)


users = []

router = APIRouter()


@router.get("/spa", response_description="Spas retrieved")
async def get_spa_list():
    spas = await retrieve_spas()
    if spas:
        return ResponseModel(spas, "Spas data retrieved successfully")
    return ResponseModel(spas, "Empty list returned")


@router.get("/spa/{id}", response_description="Spa data retrieved")
async def get_spa_data(id):
    spa = await retrieve_spa(id)
    if spa:
        return ResponseModel(spa, "Spa data retrived successfully")
    return ErrorResponseModel("An error occurred.", 404, "Spa doesn't exist.")


@router.get("/spabooking", response_description="Spas booking retrieved")
async def get_spa_booking_list():
    spas = await retrieve_spas_booking()
    if spas:
        return ResponseModel(spas, "Spas Booking data retrieved successfully")
    return ResponseModel(spas, "Empty list returned")


@router.get("/spabooking/{name}", response_description="Spa booking retrieved")
async def get_spa_booking_data(name):
    spa = await retrieve_spa_booking(name)
    if spa:
        return ResponseModel(spa, "Spa booking data retrieved successfully")
    return ResponseModel(spa, "Empty list returned")


@router.post("/signup")
async def create_user(user: OwnerSchema = Body(...)):
    users.append(user)
    return signJWT(user.email)


# define a helper function to check if a user exists
def check_user(data: OwnerLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False


# define the login route
@router.post("/login", dependencies=[Depends(JWTBearer())])
async def user_login(user: OwnerLoginSchema = Body(...)):
    if check_user(user):
        return signJWT(user.email)
    return {
        "error": "Wrong login details"
    }


@router.post("/spa/list", response_description="Spa data added into the database")
async def add_spa_data(spa: SpaSchema = Body(...)):
    spa = jsonable_encoder(spa)
    new_spa = await add_spa(spa)
    return ResponseModel(new_spa, "Spa added successfully.")

@router.post("/spa/spabooking", response_description="Spa booking data added into the database")
async def add_spa_booking_data(spa: SpaBookingSchema = Body(...)):
    spa = jsonable_encoder(spa)
    new_spa = await add_spa_booking(spa)
    return ResponseModel(new_spa, "Spa booking added successfully.")


@router.put("/update/{username}")
async def update_user_data(username: str, req: UpdateOwnerModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_user = await update_user(username, req)
    if updated_user:
        return ResponseModel(
            "User with ID: {} name update is successful".format(username),
            "User name updated successfully"
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the user data"
    )


@router.put("/spa/update/{id}")
async def update_spa_data(id: str, req: UpdateSpaModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_spa = await update_spa(id, req)
    if updated_spa:
        return ResponseModel(
            "Spa type with ID: {} name update is successful".format(id),
            "Spa type updated successfully"
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the spa data"
    )


@router.put("/spabooking/{id}")
async def update_spa_booking_data(id: str, req: UpdateSpaBookingModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_spa = await update_spa_booking(id, req)
    if updated_spa:
        return ResponseModel(
            "Spa booking with ID: {} name update is successful".format(id),
            "Spa booking updated successfully"
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the spa data"
    )


@router.delete("/delete/spa/{id}", response_description="Spa data deleted from the data base")
async def delete_spa_data(id: str):
    deleted_spa = await delete_spa(id)
    if deleted_spa:
        return ResponseModel(
            "Spa type with ID: {} removed".format(id), "Spa deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Spa type with id {0} doesn't exist".format(id)
    )


@router.delete("/delete/spabooing/{id}", response_description="Spa booking data deleted from the data base")
async def delete_spa_booking_data(id: str):
    deleted_spa = await delete_spa_booking(id)
    if deleted_spa:
        return ResponseModel(
            "Spa booking with ID: {} removed".format(id), "Spa booking deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Spa booking with id {0} doesn't exist".format(id)
    )
