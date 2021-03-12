from fastapi import FastAPI
from server.routes.user_route import router as UserRouter
from server.routes.spa_route import router as SpaRouter
from server.routes.user_access_router import router as UserAccessRouter
from server.routes.owner_access_router import router as OwnerAccessRouter
from server.routes.spa_booking_router import router as SpaBookingRouter


app = FastAPI()

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to my API!"}


app.include_router(UserAccessRouter, tags=["User access (for customer)"], prefix="/customer")
app.include_router(OwnerAccessRouter, tags=["User access (for owner)"], prefix="/owner")
app.include_router(UserRouter, tags=["User data (for config by admin)"], prefix="/configuser")
app.include_router(SpaRouter, tags=["Spa list data (for config by admin)"], prefix="/configspa")
app.include_router(SpaBookingRouter, tags=["Spa booking data (for config by admin)"], prefix="/configspabooking")

