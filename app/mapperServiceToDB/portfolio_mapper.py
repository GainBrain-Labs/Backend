from app.schemas.portfolio import CreatePortfolio, CreatePortfolioComposition
from app.models.portfolio import Portfolio, PortfolioComposition
def add_portfolio_to_db(portfolio_data: CreatePortfolio) -> Portfolio:
    return Portfolio(
        name = portfolio_data.name,
        user_id = portfolio_data.user_id
    )

def add_portfolio_composition_to_db(portfolio_composition_data: CreatePortfolioComposition) -> PortfolioComposition:
    return PortfolioComposition(
        stock_group_id = portfolio_composition_data.stock_group_id,
        portfolio_id = portfolio_composition_data.portfolio_id
    )

