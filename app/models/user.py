from app.models.base import BasicModel
from sqlalchemy import Column, String,Date,Boolean

class User(BasicModel):
    __tablename__ = "user"

    username = Column(String,unique=True, nullable=False)
    first_name = Column(String,nullable=False)
    last_name = Column(String)
    password = Column(String,nullable=False)
    email = Column(String, unique=True, nullable=False)
    profile_pic = Column(String, nullable=True)
    phone_number = Column(String, unique=True, nullable=True)
    dob = Column(Date, nullable=True)
    is_active = Column(Boolean, default=True)