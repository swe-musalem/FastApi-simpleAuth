from pydantic import BaseModel

class User(BaseModel):
  username:str
  password:str

class Data(BaseModel):
  data:str