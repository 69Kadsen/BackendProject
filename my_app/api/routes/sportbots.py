
from datetime import datetime, timedelta
from fastapi import APIRouter, Body, HTTPException
from fastapi.encoders import jsonable_encoder

from api.models.sportbots import *
from api.models.util import *

from ..db_helper import (
    create_document,
    get_document_by_id,
    get_document_by_name,
    get_document_by_sport,
    get_documents,
)


sportbots = APIRouter()

collection_name = "sportbots"


@sportbots.get("/sportbots/")
async def get_sportrollbots(collection_name: str = collection_name):
    sportbot = await get_documents(collection_name)
    if sportbot:
        return ResponseModel(sportbot, "Sportbot successfulyl retrieved from db")
    return ResponseModel(sportbot, "Empty list returned")


@sportbots.get("/sportbots/{name}")
async def get_rollbot_by_name(name, collection_name: str = collection_name):
    sportbot = await get_document_by_name(collection_name, name)
    if sportbot:
        return ResponseModel(sportbot, "Successfully retrived Sportbot {} from DB".format(name))
    return ErrorResponseModel("Error", 404, "Something went wrong retrieved from db")

@sportbots.post("/sportbots/")
async def add_rollbot_data(collection_name: str = collection_name, sportrollbot: SportbotSchema = Body(...)):
    try:
        sportrollbot = jsonable_encoder(sportrollbot)
        print(sportrollbot)
        new_sportbot = await create_document(collection_name, sportrollbot)
        print(new_sportbot)
        return ResponseModel(new_sportbot, "Sportbot added succesfully")
    except JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON format")
