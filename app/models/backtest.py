from app.models.base import BasicModel
from app.db.base import Base
from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, Enum, Float
from app.models.enums import BacktestProcessingStatus

class Backtest(BasicModel):
    __tablename__ = "backtest"
    
    name = Column(String, nullable=False)
    description = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    portfolio_id = Column(Integer, ForeignKey('portfolio.id'), nullable=False)
    strategy_id = Column(Integer, ForeignKey('strategy.id'), nullable=False)
    initial_portfolio_value = Column(Float, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    status =  Column(Enum(BacktestProcessingStatus), nullable=False)

class BacktestResultMetrics(Base):
    __tablename__ = "backtest_result_metrics"
    
    id = Column(Integer, primary_key=True)
    sharpe_ratio = Column(Float)
    max_drawdown = Column(Float)
    final_return = Column(Float)
    
class BacktestResult(BasicModel):
    __tablename__ = "backtest_result"
    
    backtest_id = Column(Integer, ForeignKey('backtest.id'), nullable=False)
    final_portfolio_value = Column(Float)
    backtest_result_metrics_id = Column(Integer, ForeignKey('backtest_result_metrics.id'), nullable=False)