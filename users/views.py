from fastapi.routing import APIRouter
from .schema import User as UserSchema,Data
from fastapi import Header,Body, Depends

import jwt

from db import SessionLocal
from .models import User

router = APIRouter()

@router.post('/register')
def register(data:UserSchema) -> None:
  connection = SessionLocal()
  
  newUser = User(username=data.username,password=data.password)
  connection.add(newUser)
  connection.commit()
  encoded_data = jwt.encode(dict(data),"secret",algorithm="HS256")
  # register to database
  return {"message":encoded_data}


# ? Add dependancy Injection


def is_authenticated(token:str = Header(...)):
  try:
    decoded_data = jwt.decode(token,"secret",algorithms=["HS256"])
    connection = SessionLocal()
    user = connection.query(User).filter(User.username == decoded_data['username'] and User.password == decoded_data['password']).first()
    if user:
      return True
    return False
  except Exception as e:
    print('token error', e)
    return False


@router.post('/login')
def login(data: Data = Body(None), isLogged:bool = Depends(is_authenticated)):
  
  return {
    "data":data,
    'isLogged':isLogged
    }