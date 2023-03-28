from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes.rollbots import rollbots
from api.routes.sportbots import sportbots
from api.routes.sports import sports
from api.routes.share import share
from api.routes.user import user

app = FastAPI()

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


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
