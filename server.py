from sanic import Sanic
from strawberry.sanic.views import GraphQLView
from infraestructure.graphql.strawberry import schema
from config import TORTOISE_ORM
from tortoise.contrib.sanic import register_tortoise

app = Sanic(__name__)

# Load Models in app
register_tortoise(
    app, config=TORTOISE_ORM, generate_schemas=False
)

# Loag GraphQL Scheema if needed
app.add_route(
    GraphQLView.as_view(schema=schema, graphiql=True),
    "/read-api",
)
