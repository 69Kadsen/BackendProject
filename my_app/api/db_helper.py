from .database import rollbots_collection, sportbots_collection, share_collection, user_collection as db
from datetime import datetime, date
from pymongo import ReturnDocument
from typing import Dict, Any

from api.models.user import InventorySchema, UserSchema

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

# update user inventory data

async def update_user_by_username(collection_name, username: str, update_data: dict):
    collection = await get_collection(collection_name)
    user_doc = await get_document_by_username(collection_name,username)

    update_data = update_data.dict()

    if user_doc and user_doc.get("inventory") is not None:

        result = await collection.update_one(
            {"username": username},
            {"$push": {"inventory": update_data}}
        )

        #result = await collection.update_one( query, update)

        if result.modified_count == 1:
            # Return the updated document
            updated_user_doc = await get_document_by_username(collection_name, username)
            return updated_user_doc
        #result["_id"] = str(result["_id"])

        return updated_user_doc
    
    return "user not found or inventory is empty"

# by Sport

async def get_document_by_sport(collection_name, document_sport):
    collection = get_collection(collection_name)
    return collection.find_one({"sport": document_sport})

async def delete_document(collection_name, document_id):
    collection = get_collection(collection_name)
    return collection.delete_one({"_id": document_id})