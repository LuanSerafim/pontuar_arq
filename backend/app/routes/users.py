from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend import models, schemas, database
from passlib.context import CryptContext

router = APIRouter(prefix="/users", tags=["Users"])
get_db = database.get_db
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Criar usuário
@router.post("/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    hashed_password = pwd_context.hash(user.password)
    new_user = models.User(name=user.name, email=user.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Listar usuários
@router.get("/", response_model=list[schemas.User])
def list_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()
