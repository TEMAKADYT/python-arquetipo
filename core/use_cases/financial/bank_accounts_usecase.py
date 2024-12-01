from core.entities.bank_account_entity import BankAccountEntity

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
