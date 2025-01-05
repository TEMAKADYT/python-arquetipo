from sanic_ext import Extend
from sanic import Sanic, Request, Websocket
from strawberry.sanic.views import GraphQLView
from strawberry.subscriptions import GRAPHQL_TRANSPORT_WS_PROTOCOL, GRAPHQL_WS_PROTOCOL
from web.graphql.strawberry import schema
from sanic import text
import asyncio

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

    app.config.CORS_ORIGINS = "http://localhost:3000,http://localhost:3010,http://localhost:5173"
    Extend(app)

    # Load Models in app
    register_tortoise(
        app, config=TORTOISE_ORM, generate_schemas=False
    )

    # Loag GraphQL Scheema if needed
    app.add_route(
        GraphQLView.as_view(schema=schema, graphiql=True),
        "/graphql",
        methods=["POST", "GET"],  # Include POST and optionally GET
        name='graphql',
    )

    return app

    # @app.websocket("/graphql-ws")
    # async def graphql_websocket(request, ws):
        # while True:
        #     await asyncio.sleep(0.5)
        #     await ws.send('{"foo": "bar"}')
        # Determine the WebSocket protocol being used
        # protocols = ws.subprotocols
        # if GRAPHQL_TRANSPORT_WS_PROTOCOL in protocols:
        #     subprotocol = GRAPHQL_TRANSPORT_WS_PROTOCOL
        # elif GRAPHQL_WS_PROTOCOL in protocols:
        #     subprotocol = GRAPHQL_WS_PROTOCOL
        # else:
        #     # Close connection if no supported protocol is found
        #     await ws.close()
        #     return

        # Accept the WebSocket connection
        # await ws.accept(subprotocol=subprotocol)

        # Pass the WebSocket connection to Strawberry's subscription handler
        # await GraphQLView.handle_websocket(ws, schema)

    # BATCH PROCCESSING
    # app.add_route(
    #     GraphQLView.as_view(schema=schema, batch=True),
    #     '/graphql/batch',
    #     name='batchgraphql',
    # )


    # BASIC POST ROUTE
    # app.add_route(
    #     hello,
    #     '/hello',
    #     methods=["POST"],
    # )
    # def hello(request: Request):
        # return text('hello world')

    # BASIC WEBSOCKET WORKS
    # app.add_websocket_route(
    #    feed,
    #   '/feed',
    # )
    # async def feed(request, ws):
        # while True:
        #     await asyncio.sleep(0.5)
        #     await ws.send('hello')
