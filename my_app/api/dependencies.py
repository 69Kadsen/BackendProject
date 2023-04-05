from typing import Annotated
from fastapi import Header, HTTPException


from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
