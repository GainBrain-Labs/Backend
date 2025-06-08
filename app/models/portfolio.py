from app.models.base import BasicModel
from sqlalchemy import Column, String, Integer, ARRAY, ForeignKey
from sqlalchemy.orm import relationship

class portfolio(BasicModel):
    __tablename__ = 'portfolio'
    
    name = Column(String(100), nullable=False, unique=True)
    stock_group_ids = Column(ARRAY(Integer), nullable=False)
    user_id = relationship("User", foreign_keys='User.id',cascade="all, delete-orphan")
