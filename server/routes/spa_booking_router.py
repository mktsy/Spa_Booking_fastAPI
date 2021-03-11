from fastapi import APIRouter, Body, Depends
from fastapi.encoders import jsonable_encoder
from server.auth.auth_handler import signJWT
from server.auth.auth_bearer import JWTBearer


from server.database.spa_booking_database import(
    retrieve_spa_booking,
    retrieve_spas_booking,
    update_spa_booking,
    delete_spa_booking,
    add_spa_booking
)
from server.model.spa_booking_schema import(
    ErrorResponseModel,
    ResponseModel,
    SpaBookingSchema,
    UpdateSpaBookingModel
)


router = APIRouter()


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


@router.post("/spa/spabooking", response_description="Spa booking data added into the database")
async def add_spa_booking_data(spa: SpaBookingSchema = Body(...)):
    spa = jsonable_encoder(spa)
    new_spa = await add_spa_booking(spa)
    return ResponseModel(new_spa, "Spa booking added successfully.")


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