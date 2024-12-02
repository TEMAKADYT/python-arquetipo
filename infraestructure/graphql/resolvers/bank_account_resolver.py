from infraestructure.db.repositories.bank_account_repository import BankAccountRepository
from core.use_cases.financial.bank_accounts_usecase import FindOneBankAccountsUseCase
from core.use_cases.financial.bank_accounts_usecase import ListBankAccountsUseCase
from core.entities.bank_account_entity import BankAccountEntity
from core.use_cases.financial.bank_accounts_usecase import CreateAccountUseCase
from core.use_cases.financial.bank_accounts_usecase import UpdateBankAccountUseCase
from core.use_cases.financial.bank_accounts_usecase import DeleteAccountUseCase

async def get_bankaccount_by_id(entity_id: int):
    repository_impl = BankAccountRepository()
    result = await FindOneBankAccountsUseCase(repository_impl).execute(entity_id)
    return result

async def get_bank_accounts():
    repository_impl = BankAccountRepository()
    result = await ListBankAccountsUseCase(repository_impl).execute()
    return result

async def create_bank_account(entity : BankAccountEntity):
    repository_impl = BankAccountRepository()
    result = await CreateAccountUseCase(repository_impl).execute(entity)
    return result

async def update_bank_account(entity : BankAccountEntity):
    repository_impl = BankAccountRepository()
    record = await UpdateBankAccountUseCase(repository_impl).execute(entity)
    return record

async def remove_bank_account(entity_id : int):
    repository_impl = BankAccountRepository()
    await DeleteAccountUseCase(repository_impl).execute(entity_id)
