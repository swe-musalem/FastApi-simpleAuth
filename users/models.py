from db  import Base
from sqlalchemy import Column,Integer,String
from db import engine

class User(Base):
  __tablename__ = 'users'
  id: int = Column(Integer,unique=True,primary_key=True,index=True,autoincrement=True)
  username:str = Column(String,index=True,unique=True)
  password:str = Column(String,index=True)

Base.metadata.create_all(bind=engine)