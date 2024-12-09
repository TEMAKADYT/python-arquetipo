from domain.entities.bank_account_entity import BankAccountEntity
from domain.repositories.crud_repository_interface import CRUDRepositoryInterface
from application.interactors.crud_interactors import CRUDInteractors

class BankAccountInteractors(CRUDInteractors[BankAccountEntity]):

    # TODO ADD repository injection
    def __init__(self, bank_account_repository : CRUDRepositoryInterface[BankAccountEntity]):
        CRUDInteractors.__init__(self, bank_account_repository)

    async def get_bankaccount_by_id(self, entity_id: int):
        result = await super().get_one_by_id(entity_id)
        return result

    async def get_bank_accounts(self):
        result = await super().get_list()
        return result

    async def create_bank_account(self, entity : BankAccountEntity):
        result = await super().create(entity)
        return result

    async def update_bank_account(self, entity : BankAccountEntity):
        record = await super().update(entity)
        return record

    async def remove_bank_account(self, entity_id : int):
        await super().remove(entity_id)
