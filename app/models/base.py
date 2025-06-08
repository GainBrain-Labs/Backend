from datetime import datetime
from db.base import Base
from sqlalchemy import Column, Integer, DateTime

class Metadata(Base):
    __tablename__ = 'metadata'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now) 
