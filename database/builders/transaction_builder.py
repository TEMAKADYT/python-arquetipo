from database.tortoiseimpl.models.transaction_model import TransactionModel
from domain.entities.transaction_entity import TransactionEntity
from tortoise.exceptions import ParamsError

def transactionFromModel(transactionModel : TransactionModel):
    return TransactionEntity(
        transactionModel.id,
        transactionModel.amount,
        transactionModel.description,
        transactionModel.date,
        transactionModel.category,
        transactionModel.type
    )


def transactionsFromQuerySet(queryset):
    try:
        return [transactionFromModel(transaction) for transaction in queryset]
    except ParamsError:
        print("transactionsFromQuerySet: ParamsError")
        return []
