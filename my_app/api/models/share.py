
from typing import Optional, List
from pydantic import BaseModel, Field
from datetime import date


class SportEntrySchema(BaseModel):
    share_value: float
    date_time: date


class SportSchema(BaseModel):
    sport: str
    bots: int
    shares: int
    shareEntry: List[SportEntrySchema] = []

    class Config:
        schema_extra = {
            "example": {
                "sport": "Boxing",
                "bots": 149,
                "shares": 420,
                "shareEntry": [
                        {"share_value": 5.28, "date_time": "2023-03-01T00:00:00"},
                        {"share_value": 14.78, "date_time": "2023-03-02T00:00:00"},
                        {"share_value": 3.32, "date_time": "2023-03-03T00:00:00"},
                ]
            }
        }


class ShareSchema(BaseModel):
    total_shares: int
    total_bots: int
    base_value: float
    total_value: float
    sports: SportSchema

    class Config:
        schema_extra = {
            "example": {
                "total_shares": 1255,
                "total_bots": 333,
                "base_value": 7.69,
                "total_value": 28125.04,
                "sports": {
                    "sport": "Boxing",
                    "bots": 149,
                    "shares": 420,
                    "shareEntry": [
                        {"share_value": 5.28, "date_time": "2023-03-01T00:00:00"},
                        {"share_value": 14.78, "date_time": "2023-03-02T00:00:00"},
                        {"share_value": 3.32, "date_time": "2023-03-03T00:00:00"},
                    ]
                }
            }
        }



