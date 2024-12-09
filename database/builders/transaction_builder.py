from database.tortoise.models.transaction_model import TransactionModel
from domain.entities.transaction_entity import TransactionEntity

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
    return [transactionFromModel(transaction) for transaction in queryset]
