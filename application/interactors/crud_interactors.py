from typing import Generic, TypeVar
from domain.repositories.crud_repository_interface import CRUDRepositoryInterface
from domain.entities.abc_entity import ABCEntity
from domain.usecases.crud_base_usecase import FindOneByIdUsecase
from domain.usecases.crud_base_usecase import ListUsecase
from domain.usecases.crud_base_usecase import CreateUsecase
from domain.usecases.crud_base_usecase import UpdateUsecase
from domain.usecases.crud_base_usecase import DeleteUsecase

# Set UpperBound for T
T = TypeVar('T', bound=ABCEntity)

class CRUDInteractors(Generic[T]):

    # TODO ADD repository injection
    def __init__(self, repository : CRUDRepositoryInterface[T]):
        self.repository = repository

    async def get_one_by_id(self, entity_id: int):
        result = await FindOneByIdUsecase(self.repository).execute(entity_id)
        return result

    async def get_list(self):
        result = await ListUsecase(self.repository).execute()
        return result

    async def create(self, entity : T):
        result = await CreateUsecase(self.repository).execute(entity)
        return result

    async def update(self, entity : T):
        record = await UpdateUsecase(self.repository).execute(entity)
        return record

    async def remove(self, entity_id : int):
        await DeleteUsecase(self.repository).execute(entity_id)

    # TODO IMPLEMENT RESTORE
    # async def restore(self, entity_id : int):
    #     await RestoreAccountUsecase(self.repository).execute(entity_id)
