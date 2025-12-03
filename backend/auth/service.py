from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.auth import models, schemas
from app.core.security import hash_password, verify_password


def create_user(db: Session, user_data: schemas.UserCreate):
    """
    Cria um novo usuário no banco.
    """
    # Verifica se o email já existe
    existing_user = db.query(models.User).filter(models.User.email == user_data.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="E-mail já está em uso."
        )

    # Criptografa senha com truncamento seguro
    hashed = hash_password(user_data.password)

    new_user = models.User(
        email=user_data.email,
        hashed_password=hashed,
        plan="free",           # plano padrão
        message_count=0        # contador padrão
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def authenticate_user(db: Session, email: str, password: str):
    """
    Verifica se o usuário existe e se a senha é válida.
    """
    user = db.query(models.User).filter(models.User.email == email).first()

    if not user:
        return None

    if not verify_password(password, user.hashed_password):
        return None

    return user


def get_user_by_id(db: Session, user_id: int):
    """
    Busca um usuário pelo ID.
    """
    return db.query(models.User).filter(models.User.id == user_id).first()
