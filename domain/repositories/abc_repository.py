from abc import ABC
from typing import Generic, TypeVar

# Set UpperBound for T
T = TypeVar('T')

class ABCRepository(ABC, Generic[T]):
    pass
