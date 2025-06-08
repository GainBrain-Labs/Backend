from base import BasicModel
from sqlalchemy import Column, String, ARRAY, Integer
from enums import stock_group_type
from enum import Enum

class stock(BasicModel):
    __tablename__ = 'stock'
    name = Column(String(100),nullable=False, unique=True)
    ticker = Column(String(20), nullable=False, unique=True, index=True)


class stock_group(BasicModel):
    __tablename__ = 'stock_group'
    name = Column(String(100), nullable=False, unique=True)
    ticker = Column(String(20), nullable=False, unique=True, index=True)
    stock_group_type =  Column(Enum(stock_group_type), nullable=False, nullable=False, unique=True)
    stock_ids = Column(ARRAY(Integer), nullable=False)


