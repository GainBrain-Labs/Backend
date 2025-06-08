from models.base import BasicModel
from db.base import Base
from sqlalchemy import Column, String,Integer, ForeignKey

class Expression(Base):
    __tablename__ = "expression"

    id = Column(Integer, primary_key=True)
    expression = Column(String,unique=True, nullable=False)

class Strategy(BasicModel):
    __tablename__ = "strategy"

    name = Column(String,unique=True, nullable=False)
    description = Column(String)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False, index=True)
    expression_id = Column(Integer, ForeignKey("expression.id"), nullable=False, index=True)
