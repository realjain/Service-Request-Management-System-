from pydantic import BaseModel,EmailStr

class UserCreate(BaseModel):
    name: str
    email:EmailStr
    phone_no:str | None=None
    password:str
    role:str

class UserLogin(BaseModel):
    email:EmailStr
    password:str
