from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer

from api.routes.rollbots import rollbots
from api.routes.sportbots import sportbots
from api.routes.sports import sports
from api.routes.share import share
from api.routes.user import user
from api.routes.auth import auth

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


origins = [
    "https://69kadsen-glorious-memory-5wv4wwxj6p6cpxr6-3000.preview.app.github.dev",
    "https://69kadsen-glorious-memory-5wv4wwxj6p6cpxr6-8000.preview.app.github.dev",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(rollbots, prefix="/api", tags=["Rollbots"])
app.include_router(sportbots, prefix="/api", tags=["Sportbots"])
app.include_router(sports, prefix="/api", tags=["Sports"])
app.include_router(share, prefix="/api", tags=["Share"])
app.include_router(user, prefix="/api", tags=["User"])
app.include_router(auth, prefix="/api", tags=["Auth"])





@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
