import strawberry
from typing import Optional

@strawberry.type
class BankAccount:
    name: str
    bank_name: str
    account_type: str
    balance: float
    id: Optional[int]
    created_at: Optional[str]
    updated_at: Optional[str]
    deleted_at: Optional[str]
