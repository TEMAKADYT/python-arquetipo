from sanic import Sanic
from strawberry.sanic.views import GraphQLView
from web.graphql.strawberry import schema

# TODO INJECT CONFIGURATION
from database.tortoiseimpl.config import TORTOISE_ORM
from tortoise.contrib.sanic import register_tortoise

# MAIN
# LOAD AND CONFIGURE CONCRETE TECHNOLOGIES
# THE MAIN FILE OF THE APPLICATION

# APP CREATE
app = Sanic('sanic_app')

# Load Models in app
register_tortoise(
    app, config=TORTOISE_ORM, generate_schemas=False
)

# Loag GraphQL Scheema if needed
app.add_route(
    GraphQLView.as_view(schema=schema, graphiql=True),
    "/gql",
    methods=["POST", "GET"],  # Include POST and optionally GET
)
