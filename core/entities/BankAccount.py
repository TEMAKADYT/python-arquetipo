# src/core/entities/bank_account.py
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class BankAccount:
    id: Optional[int]
    name: str
    bank_name: str
    account_type: str
    balance: float = 0.0

    transactions: list = field(default_factory=list)  # Lista de transacciones asociadas
