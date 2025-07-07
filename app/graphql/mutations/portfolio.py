import strawberry
from app.graphql.types.portfolio import CreatePortfolioInput,Portfolio, PortfolioComposition, CreatePortfolioCompositionInput
from typing import Optional
from app.graphql.resolvers.portfolio_resolver import add_portfolio, add_portfolio_composition

@strawberry.type
class PortfolioMutation:

    @strawberry.mutation
    def add_portfolio(portfolio: CreatePortfolioInput) -> Optional[Portfolio]:
        return add_portfolio(portfolio)
    
    @strawberry.mutation
    def add_portfolio_composition(portfolio_composition: CreatePortfolioCompositionInput) -> Optional[PortfolioComposition]:
        return add_portfolio_composition(portfolio_composition)
