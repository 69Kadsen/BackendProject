from .database import rollbots_collection, sportbots_collection, share_collection, user_collection as db
from datetime import datetime, date
from pymongo import ReturnDocument
from typing import Dict, Any

from api.schemas.user import *

from fastapi.encoders import jsonable_encoder
import json
from bson import ObjectId
from pydantic import BaseModel
import bson


# custom encoder
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        elif isinstance(obj, ObjectId):
            return str(obj)
        elif isinstance(obj, BaseModel):
            return obj.dict()
        else:
            return super().default(obj)


# Helpers

def rollbot_helper(rollbot) -> dict:
    return {
        "id": str(rollbot["_id"]),
        "name": str(rollbot["name"]),
        "number": int(rollbot["number"]),
        "image_url": str(rollbot["image_url"]),
        "stats": dict(rollbot["stats"]),
        "traits": dict(rollbot["traits"])
    }


def sportbot_helper(sportbot) -> dict:
    return {
        "id": str(sportbot["_id"]),
        "name": str(sportbot["name"]),
        "number": int(sportbot["number"]),
        "image_url": str(sportbot["image_url"]),
        "stats": dict(sportbot["stats"]),
        "traits": dict(sportbot["traits"])
    }



def share_helper(sport) -> dict:
    return {
        "id": str(sport["_id"]),
        "bots": int(sport["bots"]),
        "shares": int(sport["shares"]),
        "shareEntry": list[sport["shareEntry"]],
    }



# DB Helper
async def get_collection(collection_name):
    collection = db[collection_name]
    return collection


async def create_document(collection_name, document):
    collection = await get_collection(collection_name)
    result = await collection.insert_one(document)
    return str(result.inserted_id)

async def get_documents(collection_name):
    collection = await get_collection(collection_name)
    documents = []
    async for document in collection.find({}):
        document['_id'] = str(document['_id'])
        documents.append(document)
    
    return documents

# by ID

async def get_document_by_id(collection_name, document_id):

    collection = await get_collection(collection_name)
    return await collection.find_one({"_id": ObjectId(document_id)})

# by Name

async def get_document_by_name(collection_name, document_name):
    collection = await get_collection(collection_name)
    document = await collection.find_one({"name": document_name})
    if document:
        document["_id"] = str(document["_id"])
    return document


# sportbot by number

async def get_sportbot_by_number(collection_name, number):
    collection = await get_collection(collection_name)
    sportbot = await collection.find_one({"number": number})
    if sportbot:
        sportbot["_id"] = str(sportbot["_id"])
    return sportbot

# by username

async def get_document_by_username(collection_name, document_name):
    collection = await get_collection(collection_name)
    document = await collection.find_one({"username": document_name})
    if document:
        document["_id"] = str(document["_id"])
    return document

# hate dates

def date_to_datetime(d: date) -> datetime:
    return datetime(d.year, d.month, d.day, 0, 0, 0)


# get user inventory

async def get_user_inv(collection_name, username):
    # collection = await get_collection(collection_name)
    user = await get_document_by_username(collection_name, username)

    if user is not None:
        result = user["inventory"]

        return result
    
    return {"User is none"}


# create inv ( only works if inv is empty list)

async def create_user_inv(collection_name, username, inventory: list):
    collection = await get_collection(collection_name)
    user_doc = await get_document_by_username(collection_name, username)

    print(inventory)

    if user_doc is not None:
        if not user_doc["inventory"]:
            result = await collection.update_one(
                {"username": username},
                {"$set": {"inventory": inventory}}
            )
            if result.modified_count == 1:
                updated_user_doc = await get_document_by_username(collection_name, username)
                return updated_user_doc
        return {"User Inventory is not empty!"}
    return {"User not found"}


# update user data

async def update_user_by_username(collection_name, username: str, update_data: UpdateUserSchema):
    collection = await get_collection(collection_name)
    user_doc = await get_document_by_username(collection_name, username)

    update_data_dict = update_data.dict(exclude_unset=True)

    if user_doc is None:
        return "User not found!"

    result = await collection.update_one(
        {"username": username},
        {"$set": update_data_dict}
    )

    if "username" in update_data_dict:
        username = update_data_dict["username"]

    if result.modified_count == 1:
        # Return the updated document
        updated_user_doc = await get_document_by_username(collection_name, username)
        return updated_user_doc
    
    return "user not found or inventory is empty, or no user data was changed"


# update user inventory data

async def update_user_inventory_by_username(collection_name: str, username: str, update_data: dict, bot_number: int) -> bool:
    collection = await get_collection(collection_name)
    user = await get_document_by_username(collection_name, username)

    update_data = update_data.dict()

    # Not working yet, a lot of "Null" entrys for some reason
    for bot in user["inventory"]:
        print(bot["bot_number"])
        print(bot_number)
        if bot["bot_number"] is bot_number:
            break

    if bot is not None:
        query = {"username": username}
        update_data = {"$set": {"inventory." + str(bot_number): update_data}}
        result = await collection.update_one(query, update_data)
        return {"Bot Inventory entry changed!", result}
        
    else:
        result = await collection.update_one({"username": username}, {"$push": {"inventory": update_data}})
        return {"Bot Inventory entry added!", result}



# by Sport

async def get_document_by_sport(collection_name, document_sport):
    collection = get_collection(collection_name)
    return collection.find_one({"sport": document_sport})

async def delete_document(collection_name, document_id):
    collection = get_collection(collection_name)
    return collection.delete_one({"_id": document_id})