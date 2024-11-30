import strawberry
from strawberry.utils import typing

## === GRAPHQL DEFINITION
@strawberry.type
class Book:
    title: str
    author: str

def get_books():
    return [] # BookModel.all()


@strawberry.type
class Query:
    books: typing.List[Book] = strawberry.field(resolver=get_books)

schema = strawberry.Schema(query=Query)
