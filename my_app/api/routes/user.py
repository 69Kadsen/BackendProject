
from datetime import datetime, timedelta
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from pydantic import parse_obj_as
from typing import Dict, Any

from api.models.user import *
from api.models.util import *

from ..db_helper import (
    create_document,
    get_document_by_id,
    get_document_by_name,
    get_document_by_sport,
    get_documents,
    get_document_by_username,
    update_user_by_username,
)

import json
from bson.objectid import ObjectId

user = APIRouter()

collection_name = "user"


@user.get("/user/")
async def get_user(collection_name: str = collection_name):
    user = await get_documents(collection_name)
    if user:
        return ResponseModel(user, "User successfulyl retrieved from db")
    return ResponseModel(user, "Empty list returned")


@user.get("/user/{name}")
async def get_user_by_name(username, collection_name: str = collection_name):
    user = await get_document_by_username(collection_name, username)
    if user:
        return ResponseModel(user, "Successfully retrived User {} from DB".format(username))
    return ErrorResponseModel("Error", 404, "Something went wrong retrieved from db")


@user.post("/user/")
async def add_user_data(collection_name: str = collection_name, user: UserSchema = Body(...)):
    user = jsonable_encoder(user)
    new_user = await create_document(collection_name, user)
    print(new_user)
    return ResponseModel(new_user, "User added succesfully")



# Inventory

@user.put("/user/{username}/inventory")
async def add_item_to_inventory(username : str, item: InventorySchema, collection_name: str = collection_name):

    user = await get_document_by_username(collection_name, username)
    if user is None:
        return {"User not found"}

    updated_user = await update_user_by_username(collection_name, user["username"] , item)
    if updated_user is None:
        return {"update failed"}


    return user, updated_user