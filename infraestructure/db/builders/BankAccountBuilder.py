from origamiapp.core.entities import BankAccount
from origamiapp.infraestructure.models import BankAccountModel

def bankAccountFromModel(bankAccountModel : BankAccountModel):
    return BankAccount(
        bankAccountModel.id,
        bankAccountModel.name,
        bankAccountModel.bank_name,
        bankAccountModel.account_type,
        bankAccountModel.balance
    )

def bankAccountsFromQuerySet(queryset):
    return [bankAccountFromModel(transaction) for transaction in queryset]
