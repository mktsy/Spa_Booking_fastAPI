from fastapi import FastAPI
from routers import spa

app = FastAPI()

@app.get('/')
async def root():
    return {'Hello': 'Makiin spa shop'}

def configRouter():
    app.include_router(spa.router)

configRouter()