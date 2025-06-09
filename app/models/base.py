from datetime import datetime
from app.db.base import Base
from sqlalchemy import Column, Integer, DateTime

class BasicModel(Base):
    
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now) 
