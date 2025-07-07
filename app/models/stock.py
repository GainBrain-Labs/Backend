from app.models.base import BasicModel
from sqlalchemy import Column, String, Integer, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app.models.enums import DefaultStockGroupType

class Stock(BasicModel):
    __tablename__ = 'stock'
    name = Column(String(100),nullable=False, unique=True)
    ticker = Column(String(20), nullable=False, unique=True, index=True)
    stock_group_composition = relationship('StockGroupComposition', backref='stock', cascade='all, delete-orphan')

class StockGroup(BasicModel):
    __tablename__ = 'stock_group'
    name = Column(String(100), nullable=False)
    # in case of custom group ticker will be randomly unique(user specific) string generated 
    ticker = Column(String(20), nullable=False, unique=True, index=True)
    type =  Column(String(20), nullable=False)
    # future make type as enum with values 'default', 'custom'
    portfolio_composition = relationship('PortfolioComposition', backref='stock_group', cascade='all, delete-orphan')
    stock_group_composition = relationship('StockGroupComposition', backref='stock_group', cascade='all, delete-orphan')

    __mapper_args__ = {
        "polymorphic_identity": "stock_group",
        "polymorphic_on": type,
    }

class DefaultStockGroup(StockGroup):
    __tablename__ = 'default_stock_group'
    id = Column(Integer, ForeignKey('stock_group.id'), primary_key=True)
    stock_group_type =  Column(Enum(DefaultStockGroupType), nullable=False)

    
    __mapper_args__ = {
        "polymorphic_identity": "default",
    }

class CustomStockGroup(StockGroup):
    __tablename__ = 'custom_stock_group'
    id = Column(Integer, ForeignKey('stock_group.id'), primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": "custom",
    }


class StockGroupComposition(BasicModel):
    __tablename__ = 'stock_group_composition'
    stock_group_id = Column(Integer, ForeignKey('stock_group.id'), nullable=False)
    stock_id = Column(Integer, ForeignKey('stock.id'), nullable=False)



