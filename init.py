from tortoise import Tortoise, run_async
from config import TORTOISE_ORM

async def init():
    try:
        await Tortoise.init(config=TORTOISE_ORM)
        await Tortoise.generate_schemas()
        print("Tortoise ORM initialized!")
    except Exception as e:
        print(f"Error initializing Tortoise ORM: {e}")


run_async(init())
