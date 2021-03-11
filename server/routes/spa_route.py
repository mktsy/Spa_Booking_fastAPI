from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database.spa_database import(
    add_spa,
    delete_spa,
    retrieve_spa,
    retrieve_spas,
    update_spa
)

from server.model.spa_schema import(
    ErrorResponseModel,
    ResponseModel,
    SpaSchema,
    UpdateSpaModel
)


router = APIRouter()


@router.get("/", response_description="Spas retrieved")
async def get_spa_list():
    spas = await retrieve_spas()
    if spas:
        return ResponseModel(spas, "Spas data retrieved successfully")
    return ResponseModel(spas, "Empty list returned")


@router.get("/{id}", response_description="Spa data retrieved")
async def get_spa_data(id):
    spa = await retrieve_spa(id)
    if spa:
        return ResponseModel(spa, "Spa data retrived successfully")
    return ErrorResponseModel("An error occurred.", 404, "Spa doesn't exist.")


@router.post("/spa", response_description="Spa data added into the database")
async def add_spa_data(spa: SpaSchema = Body(...)):
    spa = jsonable_encoder(spa)
    new_spa = await add_spa(spa)
    return ResponseModel(new_spa, "Spa added successfully.")


@router.put("/spa/{id}")
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


@router.delete("/spa/{id}", response_description="Spa data deleted from the data base")
async def delete_spa_data(id: str):
    deleted_spa = await delete_spa(id)
    if deleted_spa:
        return ResponseModel(
            "Spa type with ID: {} removed".format(id), "Spa deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Spa type with id {0} doesn't exist".format(id)
    )