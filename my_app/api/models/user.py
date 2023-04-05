from typing import Optional, List
from pydantic import BaseModel, Field, EmailStr
from datetime import date, datetime, timedelta

from .sportbots import SportbotSchema


class IventorySchema(BaseModel):
    bot_number: int | None = None
    bot: SportbotSchema | None = None
    claimed: bool | None = None
    claimed_at: date | None = None
    value: float | None = None
    buy_price: float | None = None
    unlocks_in: date | None = None


class UserSchema(BaseModel):
    username: str
    email: EmailStr | None = None
    hashed_password: str
    created_at: str | None = None
    inventory: List[IventorySchema] | None = None
    status: str | None = None
    disabled: bool | None = None

    class Config:
        schema_extra = {
            "example": {
                "username": "Kadsen",
                "email": "Kadsensmail@web.de",
                "hashed_password": "MySecretPassword",
                "created_at": "",
                "inventory": [""],
                "status": "gold",
                "disabled": False,
            }
        }

    
