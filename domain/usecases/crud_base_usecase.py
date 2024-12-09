from domain.repositories.crud_repository_interface import CRUDRepositoryInterface
from domain.entities.abc_entity import ABCEntity
from typing import Generic, TypeVar

# Set UpperBound for T
T = TypeVar('T', bound=ABCEntity)

class FindOneByIdUsecase(Generic[T]):
    def __init__(self, repository : CRUDRepositoryInterface[T]):
        self.repository = repository

    async def execute(self, entity_id) -> T | None:
        record = await self.repository.get_one_by_id(entity_id)
        return record

class ListUsecase(Generic[T]):
    def __init__(self, repository : CRUDRepositoryInterface[T]):
        self.repository = repository

    async def execute(self) -> list[T]:
        list = await self.repository.get_list()
        return list

class CreateUsecase(Generic[T]):
    def __init__(self, repository : CRUDRepositoryInterface[T]):
        self.repository = repository

    async def execute(self, entity: T) -> T:
        added = await self.repository.create(entity)
        return added

class DeleteUsecase(Generic[T]):
    def __init__(self, repository : CRUDRepositoryInterface[T]):
        self.repository = repository

    async def execute(self, entity_id: int) -> bool:
        await self.repository.remove(entity_id)
        return True

class UpdateUsecase(Generic[T]):
    def __init__(self, repository : CRUDRepositoryInterface[T]):
        self.repository = repository

    async def execute(self, entity: T) -> T:
        added = await self.repository.update(entity)
        return added
