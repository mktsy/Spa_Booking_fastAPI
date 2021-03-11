from fastapi import APIRouter, Body, Depends
from fastapi.encoders import jsonable_encoder
from server.auth.auth_handler import signJWT
from server.auth.auth_bearer import JWTBearer

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

users = []


router = APIRouter()


@router.post("/customer", response_description="User data added into the database")
async def add_user_data(user: UserSchema = Body(...)):
    user = jsonable_encoder(user)
    new_user = await add_user(user)
    return ResponseModel(new_user, "User added successfully.")


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
@router.post("/customer/login", dependencies=[Depends(JWTBearer())])
async def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return signJWT(user.email)
    return {
        "error": "Wrong login details"
    }


@router.put("/customer/{username}")
async def update_user_data(username: str, req: UpdateUserModel = Body(...)):
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


@router.get("/customer/spa", response_description="Spas retrieved")
async def get_spa_list():
    spas = await retrieve_spas()
    if spas:
        return ResponseModel(spas, "Spas data retrieved successfully")
    return ResponseModel(spas, "Empty list returned")


@router.get("/customer/spa/{id}", response_description="Spa data retrieved")
async def get_spa_data(id):
    spa = await retrieve_spa(id)
    if spa:
        return ResponseModel(spa, "Spa data retrived successfully")
    return ErrorResponseModel("An error occurred.", 404, "Spa doesn't exist.")