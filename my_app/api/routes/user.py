
from datetime import datetime, timedelta
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from api.models.user import *
from api.models.util import *

from ..db_helper import (
    create_document,
    get_document_by_id,
    get_document_by_name,
    get_document_by_sport,
    get_documents,
)


user = APIRouter()

collection_name = "user"


@user.get("/user/")
async def get_user(collection_name: str = collection_name):
    user = await get_documents(collection_name)
    if user:
        return ResponseModel(user, "Sportbot successfulyl retrieved from db")
    return ResponseModel(user, "Empty list returned")


@user.get("/user/{name}")
async def get_user_by_name(name, collection_name: str = collection_name):
    user = await get_document_by_name(collection_name, name)
    if user:
        return ResponseModel(user, "Successfully retrived Sportbot {} from DB".format(name))
    return ErrorResponseModel("Error", 404, "Something went wrong retrieved from db")


@user.post("/user/")
async def add_user_data(collection_name: str = collection_name, user: UserSchema = Body(...)):
    user = jsonable_encoder(user)
    new_user = await create_document(collection_name, user)
    print(new_user)
    return ResponseModel(new_user, "Sportbot added succesfully")