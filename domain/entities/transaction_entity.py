# src/core/entities/transaction.py
from dataclasses import dataclass
from enum import Enum
from datetime import datetime
from domain.entities.abc_entity import ABCEntity

class TransactionType(Enum):
    INGRESO = "ingreso"
    GASTO = "gasto"

class AccountType(Enum):
    ACTIVO = "activo"
    PASIVO = "pasivo"

class SubAccountType(Enum):
    AC = "activo_circulante"
    AF = "activo_fijo"
    PC = "pasivo_circulante"
    PF = "pasivo_fijo"

@dataclass
class TransactionEntity(ABCEntity):
    """ Class que representa las transacciones realizadas y su clasificacion general """
    id: int
    amount: float
    type: TransactionType
    account: AccountType
    subaccount: SubAccountType
    taxable: bool
    description: str
    date: datetime
