from tortoise import Tortoise, run_async
from config import TORTOISE_ORM

async def init():
    # Initialize Tortoise with the config from config.py
    await Tortoise.init(config=TORTOISE_ORM)
    await Tortoise.generate_schemas(safe=True)  # Create tables based on your models
    print("Tortoise ORM initialized!")

run_async(init())
