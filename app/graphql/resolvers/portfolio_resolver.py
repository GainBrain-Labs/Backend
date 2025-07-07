from app.graphql.types.portfolio import Portfolio, CreatePortfolioInput, CreatePortfolioCompositionInput, PortfolioComposition
from typing import Optional
from app.core.dependencies import get_user_context
from app.mappers import portfolio_mapper

async def add_portfolio(portfolio_data:CreatePortfolioInput) -> Optional[Portfolio]:
    ctx = await get_user_context()
    portfolio_service = ctx["portfolio_service"]
    add_portfolio_input = portfolio_mapper.add_portfolio_input(portfolio_data)
    return await portfolio_service.add_portfolio(add_portfolio_input)

async def add_portfolio_composition(portfolio_composition_data:CreatePortfolioCompositionInput) -> Optional[PortfolioComposition]:
    ctx = await get_user_context()
    portfolio_service = ctx["portfolio_service"]
    add_portfolio_composition_input = portfolio_mapper.add_portfolio_composition_input(portfolio_composition_data)
    return await portfolio_service.add_portfolio_composition(add_portfolio_composition_input)
