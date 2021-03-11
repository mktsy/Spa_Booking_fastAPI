from fastapi import FastAPI
from server.routes.user_route import router as UserRouter
from server.routes.spa_route import router as SpaRouter
from server.routes.user_access_router import router as UserAccessRouter

app = FastAPI()

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to my app!"}


app.include_router(UserAccessRouter, tags=["User access (for customer)"], prefix="/user")
app.include_router(UserRouter, tags=["User data (for config by admin)"], prefix="/configuser")
app.include_router(SpaRouter, tags=["Spa List (for config by admin)"], prefix="/configspa")
