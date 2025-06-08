from app.models.base import BasicModel
from sqlalchemy import Column, String, ARRAY, Integer, Enum
from app.models.enums import stock_group_type

class stock(BasicModel):
    __tablename__ = 'stock'
    name = Column(String(100),nullable=False, unique=True)
    ticker = Column(String(20), nullable=False, unique=True, index=True)


class stock_group(BasicModel):
    __tablename__ = 'stock_group'
    name = Column(String(100), nullable=False, unique=True)
    ticker = Column(String(20), nullable=False, unique=True, index=True)
    stock_group_type =  Column(Enum(stock_group_type), nullable=False, unique=True)
    stock_ids = Column(ARRAY(Integer), nullable=False)


