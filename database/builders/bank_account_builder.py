from database.tortoiseimpl.models import BankAccountModel
from domain.entities.bank_account_entity import BankAccountEntity

def bankAccountFromModel(bankAccountModel : BankAccountModel):
    if bankAccountModel is None:
        return None

    return BankAccountEntity(
        id=bankAccountModel.id,
        name=bankAccountModel.name,
        bank_name=bankAccountModel.bank_name,
        account_type=bankAccountModel.account_type,
        balance=bankAccountModel.balance,
        created_at=bankAccountModel.created_at,
        updated_at=bankAccountModel.updated_at,
        # deleted_at=bankAccountModel.deleted_at TODO REVIEW
    )

def bankAccountsFromQuerySet(queryset):
    return [bankAccountFromModel(transaction) for transaction in queryset]
