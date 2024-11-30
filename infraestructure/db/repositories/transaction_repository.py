from pydoc import describe
from origamiapp.core.entities.Transaction import Transaction
from origamiapp.infraestructure.models import TransactionModel
from origamiapp.infraestructure.db.builders.TransactionBuilder import transactionFromModel
from origamiapp.infraestructure.db.builders.TransactionBuilder import transactionsFromQuerySet

class TransactionRepository:

    async def add(self, transaction: Transaction) -> Transaction:
        new_record = await TransactionModel.create(
            amount = transaction.amount,
            type = transaction.type,
            account = transaction.account,
            subaccount = transaction.subaccount,
            taxable = transaction.taxable,
            description = transaction.description,
            date = transaction.date,
        )
        return transactionFromModel(new_record)

    async def get_list(self) -> list:
        all = TransactionModel.all()
        return transactionsFromQuerySet(all)

    async def get_by_id(self, transaction_id: int) -> Transaction:
        record = TransactionModel.get(id=transaction_id)
        return transactionFromModel(record)

    async def remove(self, transaction_id: int) -> None:
        return TransactionModel.get(id=transaction_id).soft_delete()

    async def restore(self, transaction_id: int) -> None:
        return TransactionModel.get(id=transaction_id).restore()