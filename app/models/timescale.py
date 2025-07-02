from app.models.base import Base
from sqlalchemy import Column, Date, Integer, ForeignKey, Float, String

class BacktestResultTimescale(Base):
    __tablename__ = "backtest_result_timescale"
    
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False, primary_key=True)
    portfolio_value = Column(Float)
    backtest_result_id = Column(Integer, ForeignKey('backtest_result.id'), nullable=False)

class StockTimescale(Base):
    __tablename__ = "stock_timescale"
    
    ticker = Column(String(20), nullable=False, primary_key=True)
    date = Column(Date, nullable=False, primary_key=True)
    open_price = Column(Float)
    close_price = Column(Float)
    high_price = Column(Float)
    low_price = Column(Float)
    volume = Column(Float)  # Can be Integer but kept it float to avoid mathematical operation type errors

'''
SELECT create_hypertable('backtest_result_timescale', 'date', if_not_exists => TRUE);
SELECT create_hypertable('stock_timescale', 'date', if_not_exists => TRUE);
'''