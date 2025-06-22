from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date

class UserCreate(BaseModel):
    username: str
    first_name: str
    last_name: Optional[str]
    email: EmailStr
    password: str
    profile_pic: Optional[str]
    phone_number: Optional[str]
    dob: Optional[date]

class GetUser(BaseModel):
    email: str

class ValidateUser(BaseModel):
    email: str
    password: str

class UserOut(BaseModel):
    username: str
    first_name: str
    last_name: Optional[str]
    email: EmailStr
    profile_pic: Optional[str]
    phone_number: Optional[str]
    dob: Optional[date]
    is_active: bool

    class Config:
        orm_mode = True