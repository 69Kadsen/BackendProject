from typing import Optional
from pydantic import BaseModel, Field, EmailStr
from datetime import date


class IventorySchema(BaseModel):
    bots: dict


class UserSchema(BaseModel):
    name: str
    email: EmailStr
    password: str
    created_at: str
    inventory: IventorySchema
    status: str

    class Config:
        schema_extra = {
            "example": {
                "name": "Kadsen",
                "email": "Kadsensmail@web.de",
                "password": "MySecretPassword",
                "created_at": "",
                "inventory": {"bots": {}},
                "status": "gold"
            }
        }
