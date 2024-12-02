from core.entities.bank_account_entity import BankAccountEntity

class FindOneBankAccountsUseCase:
    def __init__(self, bankaccount_repository):
        self.bankaccount_repository = bankaccount_repository

    async def execute(self, entity_id) -> BankAccountEntity | None:
        record = await self.bankaccount_repository.get_one_by_id(entity_id)
        return record

class ListBankAccountsUseCase:
    def __init__(self, bankaccount_repository):
        self.bankaccount_repository = bankaccount_repository

    async def execute(self) -> list[BankAccountEntity]:
        list = await self.bankaccount_repository.get_list()
        return list

class CreateAccountUseCase:
    def __init__(self, bankaccount_repository):
        self.bankaccount_repository = bankaccount_repository

    async def execute(self, entity: BankAccountEntity) -> BankAccountEntity:
        added = await self.bankaccount_repository.add(entity)
        return added

class DeleteAccountUseCase:
    def __init__(self, bankaccount_repository):
        self.bankaccount_repository = bankaccount_repository

    async def execute(self, entity_id: int) -> bool:
        await self.bankaccount_repository.remove(entity_id)
        return True

class UpdateBankAccountUseCase:
    def __init__(self, bankaccount_repository):
        self.bankaccount_repository = bankaccount_repository

    async def execute(self, entity: BankAccountEntity) -> BankAccountEntity:
        added = await self.bankaccount_repository.update(entity)
        return added
