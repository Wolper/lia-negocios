import app.auth.bcrypt_patch   # forçar backend correto
from passlib.context import CryptContext
import bcrypt

# FIX: Passlib espera bcrypt.__about__.__version__
if not hasattr(bcrypt, "__about__"):
    class About:
        __version__ = "4.0.0"
    bcrypt.__about__ = About()

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
)

def hash_password(password: str) -> str:
    password = password[:72]  # proteção extra
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    plain_password = plain_password[:72]
    return pwd_context.verify(plain_password, hashed_password)
