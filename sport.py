from fastapi import FastAPI
from typing import List
from pydantic import BaseModel, Field, ObjectId

class League(BaseModel):
    id: ObjectId = Field(alias='_id')
    standing: int
    country: str
    division: int
    clubs: list[ObjectId] = Field(default=[])

class Club(BaseModel):
    id: ObjectId = Field(alias='_id')
    name: str
    market_value: int
    elot_rating: int
    titles: int
    country: str
    city: str
    players: List[ObjectId] = Field(default=[])

class Player(BaseModel):
    id: ObjectId = Field(alias='_id')
    name: str
    efficiency_index: float
    leagues: List[ObjectId] = Field(default=[])
    country: str
    position: str
    date_of_birth: str
    match_stats: dict = Field(default={})

class Home(BaseModel):
    goals: int
    possession: float
    shots: int
    shots_on_target: int

class Away(BaseModel):
    goals: int
    possession: float
    shots: int
    shots_on_target: int

class Results(BaseModel):
    home: Home
    away: Away

class Match(BaseModel):
    id: ObjectId = Field(alias='_id')
    league_id: ObjectId = Field(alias='league')
    game_week: int
    home: ObjectId
    away: ObjectId
    results: Results