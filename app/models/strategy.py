from app.models.base import BasicModel
from app.models import Base
from sqlalchemy import Column, String,Integer, ForeignKey
from sqlalchemy.orm import relationship

class Expression(Base):
    __tablename__ = "expression"

    id = Column(Integer, primary_key=True)
    expression = Column(String,unique=True, nullable=False)
    strategy = relationship('Strategy',backref='expression',cascade='all,delete-orphan')

class Strategy(BasicModel):
    __tablename__ = "strategy"

    name = Column(String,unique=True, nullable=False)
    description = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'),nullable=False)
    expression_id = Column(Integer, ForeignKey('expression.id'),nullable=False)
    backtest = relationship('Backtest', backref='strategy', cascade='all, delete-orphan')
