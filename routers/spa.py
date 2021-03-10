from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
import pymongo

router = APIRouter(
    prefix = "/spa",
    tags = ['Spa'],
    responses = {404: {
        'message': 'Not found'
    }}
)
class Spa(BaseModel): # class Coffee inheritance from BaseModel
    name: str 
    description: Optional[str] = None
    price: str

spa_db = [
    {
        'name': 'Mineral Spring Spa',
        'description': 'The spa offers hot springs and mineral springs.',
        'price': '1000-1500 baht'
    },
    {
        'name': 'Club Spa',
        'description': "Fitness-oriented spa Enhancing the performance of the body's strength",
        'price': '1200-1500 baht'
    },
]

@router.get('/')
async def showAllSpaList():
    return spa_db

@router.get('/spa/{id}') # call by ID
async def spaByID(id : int):
    spa = spa_db[id - 1] # parameter - 1
    return spa

@router.post('/spa') # create coffee
async def createSpa(spa: Spa):
    spa = spa_db.append(spa)
    return spa_db[-1]

@router.delete('/spa/{id}')
async def deleteSpa(id: int):
    spa = spa_db[id - 1]
    spa_db.pop(id - 1)
    result = {'message': f"{spa['name']} was delete!"}
    return result

@router.put('/spa/{id}')
async def updateSpa(id: int, spa: Spa):
    spa_db[id - 1].update(**spa.dict())
    result = {'message': f"Spa id {id} update successful!"}
    return result
