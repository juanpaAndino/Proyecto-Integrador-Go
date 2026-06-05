from fastapi import FastAPI, HTTPException, Depends
from sqlmodel import SQLModel, Session, create_engine, select
from pydantic import BaseModel
from models import User
from auth import hash_password, verify_password

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url, connect_args={"check_same_thread": False})

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

app = FastAPI(title="API de Autenticación con Salt & Pepper")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

def get_session():
    with Session(engine) as session:
        yield session

class UserCredentials(BaseModel):
    username: str
    password: str


@app.post("/register")
def register(user_data: UserCredentials, session: Session = Depends(get_session)):
    statement = select(User).where(User.username == user_data.username)
    existing_user = session.exec(statement).first()
    
    if existing_user:
        raise HTTPException(status_code=400, detail="El nombre de usuario ya está en uso")
    
    hashed_pwd = hash_password(user_data.password)
    
    new_user = User(username=user_data.username, password_hash=hashed_pwd)
    session.add(new_user)
    session.commit()
    session.refresh(new_user) # Refrescar para obtener el ID generado
    
    return {"message": "Usuario registrado exitosamente", "user_id": new_user.id}

@app.post("/login")
def login(user_data: UserCredentials, session: Session = Depends(get_session)):
    statement = select(User).where(User.username == user_data.username)
    db_user = session.exec(statement).first()
    
    error_msg = "Credenciales inválidas"
    
    if not db_user:
        raise HTTPException(status_code=401, detail=error_msg)
    
    if not verify_password(user_data.password, db_user.password_hash):
        raise HTTPException(status_code=401, detail=error_msg)
        
    return {"message": "Inicio de sesión exitoso", "username": db_user.username}