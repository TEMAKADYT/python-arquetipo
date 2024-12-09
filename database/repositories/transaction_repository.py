from domain.entities.TransactionEntity import TransactionEntity
from database.tortoise.models import TransactionModel
from database.builders.transaction_builder import transactionFromModel
from database.builders.transaction_builder import transactionsFromQuerySet

class TransactionRepository:

    async def create(self, transaction: TransactionEntity) -> TransactionEntity:
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

    async def get_by_id(self, transaction_id: int) -> TransactionEntity:
        record = TransactionModel.get(id=transaction_id)
        return transactionFromModel(record)

    async def remove(self, transaction_id: int) -> None:
        return TransactionModel.get(id=transaction_id).soft_delete()

    async def restore(self, transaction_id: int) -> None:
        return TransactionModel.get(id=transaction_id).restore()
