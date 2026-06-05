import os
import bcrypt
from dotenv import load_dotenv


load_dotenv()
PEPPER = os.getenv("PEPPER_SECRET", "")

def hash_password(password: str) -> str:
    
    peppered_password = password + PEPPER

    salt = bcrypt.gensalt()
    hashed_bytes = bcrypt.hashpw(peppered_password.encode('utf-8'), salt)
    return hashed_bytes.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifica si una contraseña ingresada coincide con el hash guardado."""

    peppered_password = plain_password + PEPPER
    
    return bcrypt.checkpw(
        peppered_password.encode('utf-8'), 
        hashed_password.encode('utf-8')
    )