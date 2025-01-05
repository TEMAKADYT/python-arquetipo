import strawberry
from typing import Optional


@strawberry.type
class TransactionType():
    id: Optional[int]
    amount: float
    type: str
    account: str
    subaccount: str
    taxable: bool
    description: str
    date: str

@strawberry.type
class BankAccountType():
    name: str
    bank_name: str
    account_type: str
    balance: float
    id: Optional[str]
    color: Optional[str]
    created_at: Optional[str]
    updated_at: Optional[str]
    deleted_at: Optional[str]
