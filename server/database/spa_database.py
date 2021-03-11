import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.spa_list

spa_collection = database.get_collection("spa_collection")

# helpers

def spa_helper(spa) -> dict:
    return {
        "id": str(spa["_id"]),
        "type": spa["type"],
        "description": spa["description"],
        "price": spa["price"],
        "period_time": spa["period_time"]
    }


# Retrieve all spa list present in the database
async def retrieve_spas():
    spas = []
    async for spa in spa_collection.find():
        spas.append(spa_helper(spa))
    return spas


# Add a new spa into the database
async def add_spa(spa_data: dict) -> dict: 
    spa = await spa_collection.insert_one(spa_data)
    new_spa = await spa_collection.find_one({"_id": spa.inserted_id})
    return spa_helper(new_spa)


# Retrieve a spa with a maching ID
async def retrieve_spa(id: str) -> dict:
    spa = await spa_collection.find_one({"_id": ObjectId(id)})
    if spa:
        return spa_helper(spa)


# Update a spa with a maching ID
async def update_spa(id: str, data: dict):
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
async def delete_spa(id: str):
    spa = await spa_collection.find_one({"_id": ObjectId(id)})
    if spa:
        await spa_collection.delete_one({"_id": ObjectId(id)})
        return True