import motor.motor_asyncio
from bson.objectid import ObjectId #bson comes installed as a dependency of motor.
#from decouple import config


#MONGO_DETAILS = config('MONGO_DETAILS') # read environment variable. if you delete comment "MONGO_DETAILS" You can use MongoDB atlas 
MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.users

user_collection = database.get_collection("user_collection")

# In the code above, we imported Motor, defined the connection details, and created a client via AsyncIOMotorClient.


# helpers
# create a quick helper function for parsing the results from a database query into a Python dict.

def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "password": user["password"],
        "user_type": user["user_type"]
    }


# Retrieve all users present in the database
async def retrieve_users():
    users = []
    async for user in user_collection.find():
        users.append(user_helper(user))
    return users

# Add a new user into the database
async def add_user(user_data: dict) -> dict:
    user = await user_collection.insert_one(user_data)
    new_user = await user_collection.find_one({"_id": user.inserted_id})
    return user_helper(new_user)

# Retrieve users present in the database by id
async def retrieve_user(id: str) -> dict:
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        return user_helper(user)

# Update a user with a maching username
async def update_user(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        updated_user = await user_collection.update_one({"_id": ObjectId(id)}, {"$set": data})
        if updated_user:
            return True
        return False


# Delete a user from the database
async def delete_user(id: str):
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        await user_collection.delete_one({"_id": ObjectId(id)})
        return True

# In the code above, we defined the asynchronous operations to create, read, update and delete user data in the database via motor.