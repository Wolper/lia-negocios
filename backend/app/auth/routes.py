# backend/app/auth/routes.py
from fastapi import APIRouter, Depends, HTTPException, status, Response, Cookie
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.auth import schemas, service
from app.core.security import create_access_token, create_refresh_token, decode_token
from app.auth.models import User
from app.deps.deps import get_current_user

router = APIRouter(prefix="/auth", tags=["auth"])


COOKIE_ACCESS_NAME = "access_token"
COOKIE_REFRESH_NAME = "refresh_token"


def set_auth_cookies(response: Response, access_token: str, refresh_token: str):
    # Em produção, usar secure=True e samesite="none" se estiver em domínios diferentes
    response.set_cookie(
        key=COOKIE_ACCESS_NAME,
        value=access_token,
        httponly=True,
        secure=False,
        samesite="lax",
        path="/",
    )
    response.set_cookie(
        key=COOKIE_REFRESH_NAME,
        value=refresh_token,
        httponly=True,
        secure=False,
        samesite="lax",
        path="/",
    )


def clear_auth_cookies(response: Response):
    response.delete_cookie(COOKIE_ACCESS_NAME, path="/")
    response.delete_cookie(COOKIE_REFRESH_NAME, path="/")


@router.post("/register", response_model=schemas.UserRead, status_code=201)
def register(
    user_in: schemas.UserCreate,
    db: Session = Depends(get_db),
):
    try:
        user = service.create_user(db, user_in)
        return user
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.post("/login", response_model=schemas.TokenPair)
def login(
    user_in: schemas.UserLogin,
    response: Response,
    db: Session = Depends(get_db),
):
    user = service.authenticate_user(db, user_in.email, user_in.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    access_token = create_access_token(user.email)
    refresh_token = create_refresh_token(user.email)

    set_auth_cookies(response, access_token, refresh_token)

    return schemas.TokenPair(
        access_token=access_token,
        refresh_token=refresh_token,
    )


@router.post("/refresh", response_model=schemas.TokenPair)
def refresh_token(
    response: Response,
    refresh_token: str | None = Cookie(
        default=None, alias=COOKIE_REFRESH_NAME),
):
    if not refresh_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="No refresh token",
        )
    try:
        payload = decode_token(refresh_token)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired refresh token",
        )

    if payload.get("type") != "refresh":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token type",
        )

    email = payload.get("sub")
    if not email:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token payload",
        )

    new_access = create_access_token(email)
    new_refresh = create_refresh_token(email)

    set_auth_cookies(response, new_access, new_refresh)

    return schemas.TokenPair(
        access_token=new_access,
        refresh_token=new_refresh,
    )


@router.get("/me", response_model=schemas.UserRead)
def read_me(current_user: User = Depends(get_current_user)):
    return current_user


@router.post("/logout")
def logout(response: Response):
    clear_auth_cookies(response)
    return {"detail": "Logged out"}
