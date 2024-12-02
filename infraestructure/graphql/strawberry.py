import strawberry
from strawberry.utils import typing
from core.entities.bank_account_entity import BankAccountEntity

from infraestructure.graphql.types.types import BankAccount
from infraestructure.graphql.resolvers.bank_account_resolver import get_bank_accounts, get_bankaccount_by_id, create_bank_account, remove_bank_account, update_bank_account
from infraestructure.graphql.inputs.bank_account_inputs import NewBankAccountInput, UpdateBankAccountInput

@strawberry.type
class Mutation:

    @strawberry.mutation
    async def add_bank_account(self, newBankAccountInput : NewBankAccountInput) -> BankAccount | None:
        print(newBankAccountInput)
        entity = BankAccountEntity(
           name=newBankAccountInput.name,
           bank_name=newBankAccountInput.bank_name,
           account_type=newBankAccountInput.account_type.value,
           balance=newBankAccountInput.balance)

        saved = await create_bank_account(entity)
        return BankAccount(
            id=saved.id,
            name=saved.name,
            bank_name=saved.bank_name,
            account_type=saved.account_type,
            balance=saved.balance,
            created_at=saved.created_at,
            updated_at=saved.updated_at,
            deleted_at=saved.deleted_at)

    @strawberry.mutation
    async def delete_bank_account(self, id: int) -> bool:
        await remove_bank_account(id)
        return True

    @strawberry.mutation
    async def update_bank_account(self, updateBankAccount : UpdateBankAccountInput) -> BankAccount | None:
        entity = BankAccountEntity(id=updateBankAccount.id,
           name=updateBankAccount.name,
           bank_name=updateBankAccount.bank_name,
           account_type=updateBankAccount.account_type.value,
           balance=updateBankAccount.balance)
        updated = await update_bank_account(entity)
        return BankAccount(
            id=updated.id,
            name=updated.name,
            bank_name=updated.bank_name,
            account_type=updated.account_type,
            balance=updated.balance,
            created_at=updated.created_at,
            updated_at=updated.updated_at,
            deleted_at=updated.deleted_at)

@strawberry.type
class Query:
    list_bank_accounts: typing.List[BankAccount] = strawberry.field(resolver=get_bank_accounts)
    get_bank_account: BankAccount = strawberry.field(resolver=get_bankaccount_by_id)

schema = strawberry.Schema(query=Query, mutation=Mutation)
