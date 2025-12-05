from sqlalchemy.orm import Session
from passlib.context import CryptContext

from app.auth.models import User
from app.auth.schemas import UserCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password[:72])


def verify_password(plain: str, hashed: str):
    return pwd_context.verify(plain[:72], hashed)


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user_in: UserCreate):
    hashed_password = hash_password(user_in.password)
    user = User(
        email=user_in.email,
        hashed_password=hashed_password,
        plan="free",
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user:
        return False

    if not verify_password(password, user.hashed_password):
        return False

    return user
