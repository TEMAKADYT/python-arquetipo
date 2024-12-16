from domain.entities.transaction_entity import TransactionEntity
from domain.repositories.crud_repository_interface import CRUDRepositoryInterface
from application.interactors.crud_interactors import CRUDInteractors

class TransactionInteractors(CRUDInteractors[TransactionEntity]):

    # TODO ADD repository injection
    def __init__(self, transactions_repository : CRUDRepositoryInterface[TransactionEntity]):
        CRUDInteractors.__init__(self, transactions_repository)

    async def get_transaction_by_id(self, entity_id: int):
        result = await super().get_one_by_id(entity_id)
        return result

    async def get_transactions(self):
        result = await super().get_list()
        return result

    async def create_transaction(self, entity : TransactionEntity):
        result = await super().create(entity)
        return result

    async def update_transaction(self, entity : TransactionEntity):
        record = await super().update(entity)
        return record

    async def remove_transaction(self, entity_id : int):
        await super().remove(entity_id)
