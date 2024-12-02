import strawberry
from infraestructure.graphql.enums.enums import BankAccountType

@strawberry.input
class NewBankAccountInput:
    name: str
    bank_name: str
    account_type: BankAccountType
    balance: float


@strawberry.input
class UpdateBankAccountInput:
    id: int
    name: str
    bank_name: str
    account_type: BankAccountType
    balance: float
