
from typing import Optional, List
from pydantic import BaseModel, Field
from datetime import date


# class SportSchema(BaseModel):
#     sport: str
#     bots: int
#     shares: int
#     shareEntry: List[SportEntrySchema] = []

#     class Config:
#         schema_extra = {
#             "example": {
#                 "sport": "Boxing",
#                 "bots": 149,
#                 "shares": 420,
#                 "shareEntry": [
#                         {"share_value": 5.28, "date_time": "2023-03-01T00:00:00"},
#                         {"share_value": 14.78, "date_time": "2023-03-02T00:00:00"},
#                         {"share_value": 3.32, "date_time": "2023-03-03T00:00:00"},
#                 ]
#             }
#         }


class SportEntrySchema(BaseModel):
    share_value: float = Field(None)
    date_time: date = Field(None)


class ShareSchema(BaseModel):
    sport: str = Field(None)
    total_shares: int = Field(None)
    total_bots: int  = Field(None)
    base_value: float = Field(None)
    total_value: float = Field(None)
    share_entrys: List[SportEntrySchema] = []

    class Config:
        schema_extra = {
            "example": {
                "sport": "Soccer",
                "total_shares": 1255,
                "total_bots": 333,
                "base_value": 7.69,
                "total_value": 28125.04,
                "share_entrys":  [
                        {"share_value": 5.28, "date_time": "2023-03-01T00:00:00"},
                        {"share_value": 14.78, "date_time": "2023-03-02T00:00:00"},
                        {"share_value": 3.32, "date_time": "2023-03-03T00:00:00"},
                    ]
            }
        }



