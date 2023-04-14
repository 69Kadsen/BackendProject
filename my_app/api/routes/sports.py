
from datetime import datetime, timedelta
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from api.schemas.share import *
from api.schemas.util import *

from ..db_helper import (
    create_document,
    get_document_by_id,
    get_document_by_name,
    get_document_by_sport,
    get_documents,
)

sports = APIRouter()

collection_name = "sports"

# Sports

@sports.get("/sports/")
async def get_rollbots(collection_name: str = collection_name):
    sports = await get_documents(collection_name)
    if sports:
        return ResponseModel(sports, "Rollbots successfulyl retrieved from db")
    return ResponseModel(sports, "Empty list returned")


@sports.get("/sports/{sport}")
async def get_rollbot_by_name(sport, collection_name: str = collection_name):
    sport_data = await get_document_by_name(collection_name, sport)
    if sport_data:
        return ResponseModel(sport_data, "Successfully retrived Rollbot {} from DB".format(sport))
    return ErrorResponseModel("Error", 404, "Something went wrong retrieved from db")

@sports.post("/sports/")
async def add_sport_data(collection_name: str = collection_name, sport: ShareSchema = Body(...)):
    sport_data = jsonable_encoder(sport)
    new_sport = await create_document(collection_name, sport_data)
    print(new_sport)
    return ResponseModel(new_sport, "Rollbot added succesfully")
