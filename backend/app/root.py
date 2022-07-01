import strawberry

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter

from .gpl.queries import Query
from .gpl.mutations import Mutation
from .gpl.subscriptions import Subscription

schema = strawberry.Schema(
    query=Query, mutation=Mutation, subscription=Subscription)
graphql_app = GraphQLRouter(schema)
# graphql_app = GraphQLRouter(schema, context_getter=get_context)

app = FastAPI()

origins = [
    # "http://localhost:3000",
    # "localhost:3000",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(graphql_app, prefix="/graphql")
