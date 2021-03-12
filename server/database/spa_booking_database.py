import motor.motor_asyncio
from bson.objectid import ObjectId
#from decouple import config


#MONGO_DETAILS = config('MONGO_DETAILS') # read environment variable.
MONGO_DETAILS = "mongodb://localhost:27017"


client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.spa_list

spa_collection = database.get_collection("spa_booking_collection")

# helpers

def spa_helper(spa) -> dict:
    return {
        "id": str(spa["_id"]),
        "name": spa["name"],
        "type": spa["type"],
        "price": spa["price"],
        "time": spa["time"]
    }


# Retrieve all spa list present in the database
async def retrieve_spas_booking():
    spas = []
    async for spa in spa_collection.find():
        spas.append(spa_helper(spa))
    return spas


# Add a new spa into the database
async def add_spa_booking(spa_data: dict) -> dict: 
    spa = await spa_collection.insert_one(spa_data)
    new_spa = await spa_collection.find_one({"_id": spa.inserted_id})
    return spa_helper(new_spa)


# Retrieve a spa with a maching ID
async def retrieve_spa_booking(name: str) -> dict:
    spa = await spa_collection.find_one({"name": name})
    if spa:
        return spa_helper(spa)


# Update a spa with a maching ID
async def update_spa_booking(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    spa = await spa_collection.find_one({"_id": ObjectId(id)})
    if spa:
        updated_spa = await spa_collection.update_one({"_id": ObjectId(id)}, {"$set": data})
        if updated_spa:
            return True
        return False


# Delete a spa from the database
async def delete_spa_booking(id: str):
    spa = await spa_collection.find_one({"_id": ObjectId(id)})
    if spa:
        await spa_collection.delete_one({"_id": ObjectId(id)})
        return True