import strawberry

@strawberry.type
class Portfolio:
    name : str
    user_id : int

@strawberry.input
class CreatePortfolioInput:
    name : str
    user_id : int

@strawberry.input
class CreatePortfolioCompositionInput:
    stock_group_id : int
    portfolio_id : int

@strawberry.type
class PortfolioComposition:
    stock_group_id : int
    portfolio_id : int