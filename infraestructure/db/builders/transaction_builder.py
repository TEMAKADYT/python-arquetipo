from core.entities import TransactionEntity
from infraestructure.models import TransactionModel

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
