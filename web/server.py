from sanic import Sanic
from strawberry.sanic.views import GraphQLView
from web.graphql.strawberry import schema

# TODO INJECT CONFIGURATION
from database.tortoiseimpl.config import TORTOISE_ORM
from tortoise.contrib.sanic import register_tortoise

from database.repositories.bank_account_repository import BankAccountRepository
from web.web_container import WebContainerDI
from dependency_injector.wiring import inject, Provide

# MAIN
# LOAD AND CONFIGURE CONCRETE TECHNOLOGIES
# THE MAIN FILE OF THE APPLICATION
def create_app() -> Sanic:
    """Create and return Sanic application."""
    container = WebContainerDI()

    # container.init_resources()
    container.wire(
        modules=[__name__, "web"],
        packages=['web', 'web.graphql', 'web.graphql.resolvers']
    )

    # APP CREATE
    app = Sanic('sanic_app')
    app.ctx.container = container

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

    return app
