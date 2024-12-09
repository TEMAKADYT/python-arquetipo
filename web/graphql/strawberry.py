import strawberry
from strawberry.utils import typing
from web.graphql.inputs.bank_account_inputs import NewBankAccountInput
from web.graphql.types.types import BankAccountType
from web.graphql.resolvers.bank_account_resolver import get_bank_accounts, get_bankaccount_by_id, remove_bank_account, create_bank_account, update_bank_account
from web.graphql.inputs.bank_account_inputs import UpdateBankAccountInput
from domain.entities.bank_account_entity import BankAccountEntity

@strawberry.type
class Mutation:

    @strawberry.mutation
    async def create_bank_account(self, newBankAccountInput : NewBankAccountInput) -> BankAccountType | None:

        entity = BankAccountEntity(
           name=newBankAccountInput.name,
           bank_name=newBankAccountInput.bank_name,
           account_type=newBankAccountInput.account_type.value,
           balance=newBankAccountInput.balance)

        saved = await create_bank_account(entity)
        return saved

    @strawberry.mutation
    async def delete_bank_account(self, id: int) -> bool:
        await remove_bank_account(id)
        return True

    @strawberry.mutation
    async def update_bank_account(self, updateBankAccount : UpdateBankAccountInput) -> BankAccountType | None:
        entity = BankAccountEntity(id=updateBankAccount.id,
           name=updateBankAccount.name,
           bank_name=updateBankAccount.bank_name,
           account_type=updateBankAccount.account_type.value,
           balance=updateBankAccount.balance)
        updated = await update_bank_account(entity)
        return updated

@strawberry.type
class Query:
    list_bank_accounts: typing.List[BankAccountType] = strawberry.field(resolver=get_bank_accounts)
    get_bank_account: BankAccountType = strawberry.field(resolver=get_bankaccount_by_id)

schema = strawberry.Schema(query=Query, mutation=Mutation)
