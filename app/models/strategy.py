from app.models.base import BasicModel
from app.db.base import Base
from sqlalchemy import Column, String,Integer, ForeignKey
from sqlalchemy.orm import relationship

class Expression(Base):
    __tablename__ = "expression"

    id = Column(Integer, primary_key=True)
    expression = Column(String,unique=True, nullable=False)

class Strategy(BasicModel):
    __tablename__ = "strategy"

    name = Column(String,unique=True, nullable=False)
    description = Column(String)
    user_id = relationship("User", foreign_keys='user.id',cascade="all, delete-orphan")
    expression_id = relationship("Expression", foreign_keys='expression.id',cascade="all, delete-orphan")
