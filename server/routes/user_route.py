# We'll be using the JSON Compatible Encoder from FastAPI to convert our models into a format that's JSON compatible.
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database.user_database import(
    add_user,
    delete_user,
    retrieve_user,
    retrieve_users,
    update_user
)
from server.model.user_schema import(
    ErrorResponseModel,
    ResponseModel,
    UserSchema,
    UpdateUserModel
)


router = APIRouter()


@router.get("/", response_description="Users retrieved")
async def get_users():
    users = await retrieve_users()
    if users:
        return ResponseModel(users, "Users data retrieved successfully")
    return ResponseModel(users, "Empty list returned")


@router.get("/{id}", response_description="User data retrieved")
async def get_user_data(id):
    user = await retrieve_user(id)
    if user:
        return ResponseModel(user, "User data retrived successfully")
    return ErrorResponseModel("An error occurred.", 404, "User doesn't exist.")


@router.post("/user", response_description="User data added into the database")
async def add_user_data(user: UserSchema = Body(...)):
    user = jsonable_encoder(user)
    new_user = await add_user(user)
    return ResponseModel(new_user, "User added successfully.")


@router.put("/user/{id}")
async def update_user_data(id: str, req: UpdateUserModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_user = await update_user(id, req)
    if updated_user:
        return ResponseModel(
            "User with ID: {} name update is successful".format(id),
            "User name updated successfully"
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the user data"
    )


@router.delete("/user/{id}", response_description="User data deleted from the data base")
async def delete_user_data(id: str):
    deleted_user = await delete_user(id)
    if deleted_user:
        return ResponseModel(
            "User with ID: {} removed".format(id), "User deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "User with id {0} doesn't exist".format(id)
    )