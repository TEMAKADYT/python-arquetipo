import strawberry

@strawberry.input
class NewTransactionInput:
    amount: float
    type: str
    account: str
    subaccount: str
    taxable: bool
    description: str
    date: str
    bank_account_id: str


@strawberry.input
class UpdateTransactionInput:
    id: int
    amount: float
    type: str
    account: str
    subaccount: str
    taxable: bool
    description: str
    date: str
    bank_account_id: str
