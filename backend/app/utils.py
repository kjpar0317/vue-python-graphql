import os
import jwt
import time
from configparser import ConfigParser
from typing import Any, Union, Dict

from starlette.requests import Request
from starlette.websockets import WebSocket
from strawberry.permission import BasePermission
from strawberry.types import Info

from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials


def db_set_up() -> Dict:
    """Sets up configuration for the database"""

    env = os.getenv("ENV", ".config")

    if env == ".config":
        config = ConfigParser()
        config.read(".config")
        config = config["DATABASE"]

    db_config = {
        "DB_USER_NAME": config["DB_USER_NAME"],
        "DB_USER_PASSWD": config["DB_USER_PASSWD"],
        "DB_HOST": config["DB_HOST"],
        "DB_NAME": config["DB_NAME"],
    }

    return db_config


def signJWT(user_id: str) -> Dict[str, Any]:
    expires = time.time() + 600

    config = ConfigParser()
    config.read(".config")
    config = config["JWT"]

    payload = {
        "user_id": user_id,
        "expires": expires
    }

    token = jwt.encode(payload, config["JWT_SECRET"],
                       algorithm=config["JWT_ALGORITHM"])

    return {
        "user_id": user_id,
        "token": token,
        "token_expiration": expires
    }


class VerifyJWTAuthToken(HTTPBearer):
    """Does all the token verification using PyJWT"""

    def __init__(self, auto_error: bool = True):
        super(VerifyJWTAuthToken, self).__init__(auto_error=auto_error)

        self.access_token = ""

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(VerifyJWTAuthToken, self).__call__(request)

        if credentials:
            self.access_token = credentials.credentials

            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=403, detail="Invalid authentication scheme.")
            if not self.verify():
                raise HTTPException(
                    status_code=403, detail="Invalid token or expired token.")
        else:
            raise HTTPException(
                status_code=403, detail="Invalid authorization code.")

        return True

    def verify(self) -> bool:
        isTokenValid = False

        try:
            payload = self.decodeJWT()
        except Exception as e:
            raise HTTPException(
                status_code=403, detail=str(e))

        if payload:
            isTokenValid = True
        return isTokenValid

    def decodeJWT(self) -> Union[object, None]:
        env = os.getenv("ENV", ".config")

        config = ConfigParser()
        config.read(".config")
        config = config["JWT"]

        decoded_token = jwt.decode(self.access_token, config["JWT_SECRET"], algorithms=[
                                   config["JWT_ALGORITHM"]])

        return decoded_token if decoded_token["expires"] >= time.time() else None


class IsAuthenticated(BasePermission):
    message = "User is not authenticated"

    async def has_permission(self, source: Any, info: Info, **kwargs) -> bool:
        request: Union[Request, WebSocket] = info.context["request"]

        return await VerifyJWTAuthToken()(request)
