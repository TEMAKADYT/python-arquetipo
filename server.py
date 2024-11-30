from sanic import Sanic
from strawberry.sanic.views import GraphQLView
from infraestructure.graphql.strawberry import schema

app = Sanic(__name__)

# Loag GraphQL Scheema if needed
app.add_route(
    GraphQLView.as_view(schema=schema, graphiql=True),
    "/read-api",
)
