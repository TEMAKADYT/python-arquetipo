from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "bank_accounts" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "created_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "deleted_at" TIMESTAMP,
    "name" VARCHAR(100) NOT NULL,
    "bank_name" VARCHAR(100) NOT NULL,
    "account_type" VARCHAR(10) NOT NULL,
    "balance" REAL NOT NULL  DEFAULT 0
);
CREATE TABLE IF NOT EXISTS "transactions" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "created_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "deleted_at" TIMESTAMP,
    "amount" REAL NOT NULL,
    "type" VARCHAR(10) NOT NULL,
    "account" VARCHAR(10),
    "subaccount" VARCHAR(60),
    "taxable" INT NOT NULL  DEFAULT 0,
    "description" TEXT,
    "date" TIMESTAMP NOT NULL,
    "bank_account_id" INT NOT NULL REFERENCES "bank_accounts" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSON NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
