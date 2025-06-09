from app.models.base import BasicModel
from sqlalchemy import Column, String, ARRAY, Integer, Enum, ForeignKey
from app.models.enums import StockGroupType

class Stock(BasicModel):
    __tablename__ = 'stock'
    name = Column(String(100),nullable=False, unique=True)
    ticker = Column(String(20), nullable=False, unique=True, index=True)

class StockGroupBase:
    name = Column(String(100), nullable=False, unique=True)
    ticker = Column(String(20), nullable=False, unique=True, index=True)
    stock_group_type =  Column(Enum(StockGroupType), nullable=False)
    stock_ids = Column(ARRAY(Integer), nullable=False)


class StockGroup(StockGroupBase,BasicModel):
    __tablename__ = 'stock_group'

class SustomStockGroup(StockGroupBase,BasicModel):
    __tablename__ = 'custom_stock_group'
    user_id = Column(Integer,ForeignKey('user.id'), nullable=False)



