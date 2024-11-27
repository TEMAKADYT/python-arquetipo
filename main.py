from sanic import Sanic
from strawberry.sanic.views import GraphQLView
import strawberry
from strawberry.utils import typing
from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.sanic import register_tortoise
from tortoise import Tortoise, run_async
from config import TORTOISE_ORM

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

# ## === ORM DEFINITION

# class BookModel(Model):
#     id = fields.IntField(primary_key=True)
#     title = fields.CharField(max_length=255)
#     author = fields.CharField(max_length=255)

#     # Defining ``__str__`` is also optional, but gives you pretty
#     # represent of model in debugger and interpreter
#     def __str__(self):
#         return self.title + " - " + self.author

# # register_tortoise(
# #     app, db_url="postgres://postgres:12345678@localhost:55432/sanictest", modules={"models": ["server"]}, generate_schemas=True
# # )


# async def init():
#     await Tortoise.init(config=TORTOISE_ORM)
#     await Tortoise.generate_schemas()  # Automatically generates database tables for your models
#     print("Tortoise ORM initialized!")

# if __name__ == "__main__":
#     run_async(init())

async def init():
    # Initialize Tortoise with the config from config.py
    await Tortoise.init(config=TORTOISE_ORM)
    await Tortoise.generate_schemas()  # Create tables based on your models
    print("Tortoise ORM initialized!")

if __name__ == "__main__":
    run_async(init())

schema = strawberry.Schema(query=Query)
app = Sanic(__name__)


app.add_route(
    GraphQLView.as_view(schema=schema, graphiql=True),
    "/read-api",
)
