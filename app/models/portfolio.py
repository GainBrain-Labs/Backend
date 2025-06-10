from app.models.base import BasicModel
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Portfolio(BasicModel):
    __tablename__ = 'portfolio'
    
    name = Column(String(100), nullable=False, unique=True)
    user_id = Column(Integer, ForeignKey('user.id'),nullable=False)
    portfolio_composition = relationship('PortfolioComposition',backref='portfolio',cascade='all, delete-orphan')


class PortfolioComposition(BasicModel):
    __tablename__ = 'portfolio_composition'

    portfolio_id = Column(Integer, ForeignKey('portfolio.id'), nullable=False)
    stock_group_id = Column(Integer, ForeignKey('stock_group.id'), nullable=False)
