# src/core/entities/bank_account.py
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class BankAccountEntity:
    name: str
    bank_name: str
    account_type: str
    balance: float = 0.0

    id: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None

    transactions: Optional[list] = field(default_factory=list)  # Lista de transacciones asociadas
