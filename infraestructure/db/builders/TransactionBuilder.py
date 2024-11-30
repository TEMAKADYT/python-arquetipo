from origamiapp.core.entities import Transaction
from origamiapp.infraestructure.models import TransactionModel

def transactionFromModel(transactionModel : TransactionModel):
    return Transaction(
        transactionModel.id,
        transactionModel.amount,
        transactionModel.description,
        transactionModel.date,
        transactionModel.category,
        transactionModel.type
    )


def transactionsFromQuerySet(queryset):
    return [transactionFromModel(transaction) for transaction in queryset]
