from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "bank_accounts" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" VARCHAR(100) NOT NULL,
    "bank_name" VARCHAR(100) NOT NULL,
    "account_type" VARCHAR(10) NOT NULL,
    "balance" REAL NOT NULL  DEFAULT 0
);
        CREATE TABLE IF NOT EXISTS "transactions" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "amount" REAL NOT NULL,
    "type" VARCHAR(10) NOT NULL,
    "account" VARCHAR(10) NOT NULL,
    "subaccount" VARCHAR(60) NOT NULL,
    "taxable" INT NOT NULL,
    "description" TEXT NOT NULL,
    "date" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "bank_account_id" INT NOT NULL REFERENCES "bank_accounts" ("id") ON DELETE CASCADE
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "bank_accounts";
        DROP TABLE IF EXISTS "transactions";"""
