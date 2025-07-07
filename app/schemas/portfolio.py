from pydantic import BaseModel

class CreatePortfolio(BaseModel):
    name: str
    user_id: int

class CreatePortfolioComposition(BaseModel):
    portfolio_id : int
    stock_group_id : int