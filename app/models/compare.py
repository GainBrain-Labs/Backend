from app.models.base import BasicModel
from app.db.base import Base
from sqlalchemy import Column, Enum, Integer, ForeignKey, String
from app.models.enums import CompareType

class Compare(BasicModel):
    __tablename__ = "compare"
    
    name = Column(String, nullable=False)
    compare_type =  Column(Enum(CompareType), nullable=False)

class CompareBacktestComposition(Base):
    __tablename__ = "compare_backtest_composition"
    
    id = Column(Integer, primary_key=True)
    compare_id = Column(Integer, ForeignKey('compare.id'), nullable=False)
    backtest_id = Column(Integer, ForeignKey('backtest.id'), nullable=False)

