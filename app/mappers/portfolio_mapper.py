from app.graphql.types.portfolio import CreatePortfolioInput, CreatePortfolioCompositionInput
from app.schemas.portfolio import CreatePortfolio, CreatePortfolioComposition

def add_portfolio_input(portfolio_data: CreatePortfolioInput) -> CreatePortfolio:
    return CreatePortfolio(
        name = portfolio_data.name,
        user_id = portfolio_data.user_id
    )

def add_portfolio_composition_input(portfolio_composition_data: CreatePortfolioCompositionInput) -> CreatePortfolioComposition:
    return CreatePortfolioComposition(
        stock_group_id = portfolio_composition_data.stock_group_id,
        portfolio_id = portfolio_composition_data.portfolio_id
    )