import strawberry
from strawberry.utils import typing
from infraestructure.db.repositories.bank_account_repository import BankAccountRepository
from core.use_cases.financial.bank_accounts_usecase import ListBankAccountsUseCase
from typing import Optional
from core.entities.bank_account_entity import BankAccountEntity
from core.use_cases.financial.bank_accounts_usecase import CreateAccountUseCase

@strawberry.type
class BankAccount:
    name: str
    bank_name: str
    account_type: str
    balance: float
    id: Optional[int]
    created_at: Optional[str]
    updated_at: Optional[str]
    deleted_at: Optional[str]

async def get_bank_accounts():
    repository_impl = BankAccountRepository()
    result = await ListBankAccountsUseCase(repository_impl).execute()
    return result

async def create_bank_account(entity : BankAccountEntity):
    repository_impl = BankAccountRepository()
    result = await CreateAccountUseCase(repository_impl).execute(entity)
    return result

@strawberry.type
class Mutation:

    @strawberry.mutation
    async def add_bank_account(self, name: str, bank_name: str, account_type: str, balance: float) -> BankAccount | None:
       entity = BankAccountEntity(name=name, bank_name=bank_name, account_type=account_type, balance=balance)
       saved = await create_bank_account(entity)
       if saved is not None:
           return BankAccount(
               id=saved.id,
               name=saved.name,
               bank_name=saved.bank_name,
               account_type=saved.account_type,
               balance=saved.balance,
               created_at=saved.created_at,
               updated_at=saved.updated_at,
               deleted_at=saved.deleted_at)

@strawberry.type
class Query:
    bank_accounts: typing.List[BankAccount] = strawberry.field(resolver=get_bank_accounts)


schema = strawberry.Schema(query=Query,  mutation=Mutation)
