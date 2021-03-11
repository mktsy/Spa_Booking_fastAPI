from fastapi import APIRouter, Body, Depends
from fastapi.encoders import jsonable_encoder
from server.auth.auth_handler import signJWT
from server.auth.auth_bearer import JWTBearer

from server.database.user_database import(
    update_user
)
from server.database.spa_database import(
    retrieve_spas,
)
from server.database.spa_booking_database import(
    add_spa_booking,
    update_spa_booking,
    delete_spa_booking,
    retrieve_spa_booking
)
from server.model.user_schema import(
    ErrorResponseModel,
    ResponseModel,
    UserSchema,
    UpdateUserModel,
    UserLoginSchema
)
from server.model.spa_booking_schema import(
    ErrorResponseModel,
    ResponseModel,
    SpaBookingSchema,
    UpdateSpaBookingModel
)

users = []


router = APIRouter()


@router.get("/customer/spa", response_description="Spas retrieved")
async def get_spa_list():
    spas = await retrieve_spas()
    if spas:
        return ResponseModel(spas, "Spas data retrieved successfully")
    return ResponseModel(spas, "Empty list returned")



@router.get("/customer/spabooking/{name}", response_description="Spas retrieved")
async def get_spa_booking_list(name):
    spas = await retrieve_spa_booking(name)
    if spas:
        return ResponseModel(spas, "Spas booking data retrieved successfully")
    return ResponseModel(spas, "Empty list returned")
@router.post("/customer/signup")
async def create_user(user: UserSchema = Body(...)):
    users.append(user)
    return signJWT(user.email)


# define a helper function to check if a user exists
def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False

# define the login route
@router.post("/login", dependencies=[Depends(JWTBearer())])
async def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return signJWT(user.email)
    return {
        "error": "Wrong login details"
    }


@router.post("/spabooking", response_description="Spa booking data added into the database")
async def add_spa_booking_data(spa: SpaBookingSchema = Body(...)):
    spa = jsonable_encoder(spa)
    new_spa = await add_spa_booking(spa)
    return ResponseModel(new_spa, "Spa booking added successfully.")


@router.put("/{id}")
async def update_user_data(id: str, req: UpdateUserModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_user = await update_user(id, req)
    if updated_user:
        return ResponseModel(
            "User with email: {} name update is successful".format(id),
            "User name updated successfully"
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the user data"
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


@router.delete("/spabooing/{id}", response_description="Spa booking data deleted from the data base")
async def delete_spa_booking_data(id: str):
    deleted_spa = await delete_spa_booking(id)
    if deleted_spa:
        return ResponseModel(
            "Spa booking with ID: {} removed".format(id), "Spa booking deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Spa booking with id {0} doesn't exist".format(id)
    )
