from abc import ABC
from abc import abstractmethod
from domain.entities.abc_entity import ABCEntity
from typing import Generic, TypeVar
from domain.repositories.abc_repository import ABCRepository

# Set UpperBound for T
T = TypeVar('T', bound=ABCEntity)

# Interface for CRUD operations
# with async methods and generic designed types

class CRUDRepositoryInterface(ABCRepository, ABC, Generic[T]):

    @abstractmethod
    async def get_one_by_id(self, id: int | str) -> T:
        pass

    @abstractmethod
    async def get_list(self) -> list[T]:
        pass

    @abstractmethod
    async def create(self, entity : T) -> T:
        pass

    @abstractmethod
    async def update(self, entity : T) -> T:
        pass

    @abstractmethod
    async def remove(self, id: int | str) -> None:
        pass

    @abstractmethod
    async def restore(self, id: int | str) -> None:
        pass
