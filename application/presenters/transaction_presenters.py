from dataclasses import dataclass

from domain.entities.transaction_entity import TransactionEntity
from web.graphql.types.types import TransactionType

@dataclass
class TransactionPresenter:
    data: TransactionEntity | None

    def presentToStrawerryType(self) -> TransactionType:
       return TransactionType(
           id=self.data.id,
           amount=self.data.amount,
           type=self.data.type,
           account=self.data.account,
           subaccount=self.data.subaccount,
           taxable=self.data.taxable,
           description=self.data.description,
           date=self.data.date
        )



@dataclass
class TransactionListPresenter:
    data: list[TransactionEntity]

    def presentToStrawerryType(self) -> list[TransactionType]:
        return [TransactionType(id=it.id,
        name=it.name,
        bank_name=it.bank_name,
        account_type=it.account_type,
        balance=it.balance,
        created_at=it.created_at,
        updated_at=it.updated_at,
        deleted_at=it.deleted_at) for it in self.data]
