from typing import Optional
from pydantic import BaseModel, Field


class StatsSchema(BaseModel):
    profitshare_shares: int = Field(None)
    freebet: int = Field(None)
    comboboost: int = Field(None)


class TraitsSchema(BaseModel):
    sport: str = Field(None)
    background: str = Field(None)
    body: str = Field(None)
    eyes: str = Field(None)
    mouth: str = Field(None)


class SportbotSchema(BaseModel):
    name: str
    number: int
    image_url: str
    revealed: bool
    stats: Optional[StatsSchema] = None
    traits: Optional[TraitsSchema] = None

    class Config:
        schema_extra = {
            "example": {
                "name": "Sportbot#28",
                "number": 28,
                "image_url": "https://somerandomurl.2523525",
                "revealed": True,
                "stats": {"profitshare_shares": 10, "freebet": 28, "comboboost": 103},
                "traits": {"sport": "Boxing", "background": "purple", "body": "gold", "eyes": "rusty-eyes", "mouth": "rusty-mouth"}
            }
        }