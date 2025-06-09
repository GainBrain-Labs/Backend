from app.models.base import BasicModel
from sqlalchemy import Column, String, Integer, ARRAY, Integer, ForeignKey

class Portfolio(BasicModel):
    __tablename__ = 'portfolio'
    
    name = Column(String(100), nullable=False, unique=True)
    stock_group_ids = Column(ARRAY(Integer), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'),nullable=False)
