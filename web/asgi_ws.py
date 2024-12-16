from strawberry.subscriptions import GRAPHQL_TRANSPORT_WS_PROTOCOL, GRAPHQL_WS_PROTOCOL
from web.graphql.strawberry import schema
from strawberry.asgi import GraphQL
from web.web_container import WebContainerDI

container = WebContainerDI()
container.wire(
    modules=[__name__, "web"],
    packages=['web', 'web.graphql', 'web.graphql.resolvers']
)

wsapp = GraphQL(
    schema,
    subscription_protocols=[
        GRAPHQL_TRANSPORT_WS_PROTOCOL,
        GRAPHQL_WS_PROTOCOL,
    ],
)
