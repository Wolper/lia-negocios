# backend/app/core/security.py
from datetime import datetime, timedelta
from typing import Any, Dict

from jose import jwt, JWTError
from passlib.context import CryptContext

from app.core.config import get_settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(plain_password: str) -> str:
    return pwd_context.hash(plain_password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_token(data: Dict[str, Any], expires_delta: timedelta) -> str:
    settings = get_settings()
    to_encode = data.copy()
    to_encode["exp"] = datetime.utcnow() + expires_delta
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm="HS256")
    return encoded_jwt


def create_access_token(subject: str) -> str:
    settings = get_settings()
    expire = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return create_token({"sub": subject, "type": "access"}, expire)


def create_refresh_token(subject: str) -> str:
    settings = get_settings()
    expire = timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    return create_token({"sub": subject, "type": "refresh"}, expire)


def decode_token(token: str) -> Dict[str, Any]:
    settings = get_settings()
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        return payload
    except JWTError:
        raise
