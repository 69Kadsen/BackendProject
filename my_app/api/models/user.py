from typing import Optional, List
from pydantic import BaseModel, Field, EmailStr
from datetime import date, datetime, timedelta

from .sportbots import SportbotSchema


class InventorySchema(BaseModel):
    bot_number: int | None = None
    bot: SportbotSchema | None = None
    claimed: bool | None = None
    claimed_at: datetime | None = None
    value: float | None = None
    buy_price: float | None = None
    unlocks_in: datetime | None = None


class UserSchema(BaseModel):
    username: str
    email: EmailStr | None = None
    hashed_password: str
    created_at: str | None = None
    inventory: List[InventorySchema] = []
    status: str | None = None
    disabled: bool | None = None

    class Config:
        schema_extra = {
            "example": {
                "username": "johndoe",
                "email": "johndoe@example.com",
                "hashed_password": "somehash",
                "created_at": "2022-01-01T00:00:00Z",
                "inventory": [
                    {
                        "bot_number": 1,
                        "bot": {
                            "name": "Sportbot 1",
                            "number": 123,
                            "image_url": "https://example.com/images/sportbot1.png",
                            "revealed": True,
                            "stats": {
                                "sportshares": 10,
                                "freebet": 5,
                                "comboboost": 2
                            },
                            "traits": {
                                "sport": "Football",
                                "background": "Green",
                                "body": "Muscular",
                                "eyes": "Brown",
                                "teeth": "White"
                            }
                        },
                        "claimed": True,
                        "claimed_at": "2022-03-15T08:00:00Z",
                        "value": 100.0,
                        "buy_price": 50.0,
                        "unlocks_in": "2022-03-15T08:00:00Z",
                    },
                    {
                        "bot_number": 2,
                        "bot": {
                            "name": "Sportbot 2",
                            "number": 456,
                            "image_url": "https://example.com/images/sportbot2.png",
                            "revealed": False,
                            "stats": {
                                "sportshares": 5,
                                "freebet": 2,
                                "comboboost": 1
                            },
                            "traits": {
                                "sport": "Basketball",
                                "background": "Blue",
                                "body": "Tall",
                                "eyes": "Green",
                                "teeth": "Yellow"
                            }
                        },
                        "claimed": False,
                        "claimed_at": "2022-03-15T08:00:00Z",
                        "value": 50.0,
                        "buy_price": 25.0,
                        "unlocks_in": "2022-03-15T08:00:00Z",
                    }
                ],
                "status": "active",
                "disabled": False
            }
        }

    
