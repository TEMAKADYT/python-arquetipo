import strawberry
from web.graphql.enums.enums import BankAccountTypeEnum

@strawberry.input
class NewBankAccountInput:
    name: str
    bank_name: str
    account_type: BankAccountTypeEnum
    balance: float


@strawberry.input
class UpdateBankAccountInput:
    id: int
    name: str
    bank_name: str
    account_type: BankAccountTypeEnum
    balance: float
