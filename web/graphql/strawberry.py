import strawberry
from strawberry.utils import typing
from web.graphql.inputs.bank_account_inputs import NewBankAccountInput
from web.graphql.types.types import BankAccountType, TransactionType
from web.graphql.resolvers.bank_account_resolver import get_bank_accounts, get_bankaccount_by_id, remove_bank_account, create_bank_account, update_bank_account
from web.graphql.resolvers.transactions_resolvers import get_transactions, get_transaction_by_id, remove_transaction, create_transaction, update_transaction

from web.graphql.inputs.bank_account_inputs import UpdateBankAccountInput
from domain.entities.bank_account_entity import BankAccountEntity
from domain.entities.transaction_entity import TransactionEntity
from web.graphql.inputs.transaction_inputs import NewTransactionInput
from web.graphql.inputs.transaction_inputs import UpdateTransactionInput
from typing import AsyncGenerator
import asyncio

@strawberry.type
class Mutation:

    @strawberry.mutation
    async def create_bank_account(self, newBankAccountInput : NewBankAccountInput) -> BankAccountType | None:

        entity = BankAccountEntity(
           name=newBankAccountInput.name,
           bank_name=newBankAccountInput.bank_name,
           account_type=newBankAccountInput.account_type.value,
           balance=newBankAccountInput.balance,
           color=newBankAccountInput.color)

        saved = await create_bank_account(entity)
        return saved

    @strawberry.mutation
    async def delete_bank_account(self, id: int) -> bool:
        await remove_bank_account(id)
        return True

    @strawberry.mutation
    async def update_bank_account(self, updateBankAccountInput : UpdateBankAccountInput) -> BankAccountType | None:
        entity = BankAccountEntity(id=updateBankAccountInput.id,
           name=updateBankAccountInput.name,
           bank_name=updateBankAccountInput.bank_name,
           account_type=updateBankAccountInput.account_type.value,
           balance=updateBankAccountInput.balance,
           color=updateBankAccountInput.color)
        updated = await update_bank_account(entity)
        return updated

    @strawberry.mutation
    async def create_transaction(self, newTransactionInput : NewTransactionInput) -> TransactionType | None:
        entity = TransactionEntity(
            bank_account=newTransactionInput.bank_account_id,
            transaction_type=newTransactionInput.transaction_type.value,
            amount=newTransactionInput.amount,
            description=newTransactionInput.description,
            date=newTransactionInput.date
        )
        saved = await create_transaction(entity)
        return saved

    @strawberry.mutation
    async def delete_transaction(self, id: int) -> bool:
        await remove_transaction(id)
        return True

    @strawberry.mutation
    async def update_transaction(self, updateTranasctionInput : UpdateTransactionInput) -> TransactionType | None:
        entity = TransactionEntity(
            id=updateTranasctionInput.id,
            bank_account=updateTranasctionInput.bank_account_id,
            transaction_type=updateTranasctionInput.transaction_type.value,
            amount=updateTranasctionInput.amount,
            description=updateTranasctionInput.description,
            date=updateTranasctionInput.date
        )
        updated = await update_transaction(entity)
        return updated

@strawberry.type
class Subscription:
    @strawberry.subscription
    async def count(self, target: int = 100) -> AsyncGenerator[int, None]:
        for i in range(target):
            yield i
            await asyncio.sleep(0.5)


@strawberry.type
class Query:
    list_bank_accounts: typing.List[BankAccountType] = strawberry.field(resolver=get_bank_accounts)
    get_bank_account: BankAccountType = strawberry.field(resolver=get_bankaccount_by_id)

    list_transactions: typing.List[TransactionType] = strawberry.field(resolver=get_transactions)
    get_transaction: TransactionType = strawberry.field(resolver=get_transaction_by_id)

schema = strawberry.Schema(query=Query, mutation=Mutation, subscription=Subscription)
