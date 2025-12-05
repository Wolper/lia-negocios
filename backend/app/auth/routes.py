from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.auth.schemas import UserCreate, UserLogin, UserRead, TokenPair
from app.auth.service import create_user, authenticate_user
from app.core.security import create_access_token, create_refresh_token
from app.auth.security import get_current_user

router = APIRouter(prefix="/auth", tags=["Auth"])


# ---------------------------
# REGISTER
# ---------------------------
@router.post("/register", response_model=UserRead, status_code=201)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    user = create_user(db, user_in)
    return user


# ---------------------------
# LOGIN
# ---------------------------
@router.post("/login", response_model=TokenPair)
def login(user_in: UserLogin, db: Session = Depends(get_db)):
    user = authenticate_user(db, user_in.email, user_in.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    access_token = create_access_token(str(user.id))
    refresh_token = create_refresh_token(str(user.id))

    return TokenPair(access_token=access_token, refresh_token=refresh_token)


# ---------------------------
# REFRESH
# ---------------------------
@router.post("/refresh", response_model=TokenPair)
def refresh(refresh_token: str, db: Session = Depends(get_db)):
    from jose import jwt, JWTError
    from app.core.config import settings

    try:
        payload = jwt.decode(
            refresh_token, settings.SECRET_KEY, algorithms=[settings.JWT_ALGORITHM]
        )
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired refresh token")

    if payload.get("type") != "refresh":
        raise HTTPException(status_code=401, detail="Invalid token type")

    user_id = payload.get("sub")

    new_access = create_access_token(user_id)
    new_refresh = create_refresh_token(user_id)

    return TokenPair(
        access_token=new_access,
        refresh_token=new_refresh,
    )


# ---------------------------
# ME (PROTECTED)
# ---------------------------
@router.get("/me", response_model=UserRead)
def read_me(current_user=Depends(get_current_user)):
    return current_user
