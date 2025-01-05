from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "bank_accounts" ADD "color" VARCHAR(10) NOT NULL  DEFAULT '#facc15';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "bank_accounts" DROP COLUMN "color";"""
