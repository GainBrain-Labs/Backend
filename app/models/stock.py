from app.models.base import BasicModel
from sqlalchemy import Column, String, ARRAY, Integer, Enum, ForeignKey
from app.models.enums import stock_group_type

class stock(BasicModel):
    __tablename__ = 'stock'
    name = Column(String(100),nullable=False, unique=True)
    ticker = Column(String(20), nullable=False, unique=True, index=True)

class stock_group_base:
    name = Column(String(100), nullable=False, unique=True)
    ticker = Column(String(20), nullable=False, unique=True, index=True)
    stock_group_type =  Column(Enum(stock_group_type), nullable=False)
    stock_ids = Column(ARRAY(Integer), nullable=False)


class stock_group(stock_group_base,BasicModel):
    __tablename__ = 'stock_group'

class custom_stock_group(stock_group_base,BasicModel):
    __tablename__ = 'custom_stock_group'
    user_id = Column(Integer,ForeignKey('user.id'), nullable=False)



