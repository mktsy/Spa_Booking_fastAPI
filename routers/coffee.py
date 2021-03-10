from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

router = APIRouter(
    prefix = '/coffee',
    tags = ['Coffee'],
    responses = {404: {
        'message': 'Not found'
    }}
)

class Coffee(BaseModel): # class Coffee inheritance from BaseModel
    name: str 
    description: Optional[str] = None
    price: float
    quality: int

coffee_db = [
    {
        'name': 'Espresso',
        'description': 'Black coffee',
        'price': 60,
        'quality': 5
    },
    {
        'name': 'Americano',
        'description': 'Espresso 1 shot',
        'price': 55,
        'quality': 5
    }
]

@router.get('/')
async def showAllCoffee():
    return coffee_db

@router.get('/coffee/{id}') # call by ID
async def coffeeByID(id : int):
    coffee = coffee_db[id - 1] # parameter - 1
    return coffee

@router.post('/coffee') # create coffee
async def createCoffee(coffee: Coffee):
    coffee = coffee_db.append(coffee)
    return coffee_db[-1]

@router.delete('/coffee/{id}')
async def deleteCoffee(id: int):
    coffee = coffee_db[id - 1]
    coffee_db.pop(id - 1)
    result = {'message': f"{coffee['name']} was delete!"}
    return result

@router.put('/coffee/{id}')
async def updateCoffee(id: int, coffee: Coffee):
    coffee_db[id - 1].update(**coffee.dict())
    result = {'message': f"Coffee id {id} update successful!"}
    return result
