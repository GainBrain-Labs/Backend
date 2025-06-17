from fastapi import APIRouter
from app.graphql.schema import schema
from strawberry.asgi import GraphQL

router = APIRouter()

router.add_route("/",GraphQL(schema))