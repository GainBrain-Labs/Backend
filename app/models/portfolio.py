from base import BasicModel
from sqlalchemy import Column, String, Integer, ARRAY, ForeignKey, Mapped, mapped_column

class portfolio(BasicModel):
    __tablename__ = 'portfolio'
    
    name = Column(String(100), nullable=False, unique=True)
    stock_group_ids = Column(ARRAY(Integer), nullable=False)
    user_id = Mapped[int] = mapped_column(Integer, ForeignKey(name="user.id"), nullable=False, index=True) 