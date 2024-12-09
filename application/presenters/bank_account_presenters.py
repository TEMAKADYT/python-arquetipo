from typing import Optional
from dataclasses import dataclass
from domain.entities.bank_account_entity import BankAccountEntity
from web.graphql.types.types import BankAccountType

@dataclass
class BankAccountPresenter:
    data: BankAccountEntity | None

    def presentToStrawerryType(self) -> BankAccountType:
       return BankAccountType(
            id=self.data.id,
            name=self.data.name,
            bank_name=self.data.bank_name,
            account_type=self.data.account_type,
            balance=self.data.balance,
            created_at=self.data.created_at,
            updated_at=self.data.updated_at,
            deleted_at=self.data.deleted_at
        )


@dataclass
class BankAccountListPresenter:
    data: list[BankAccountEntity]

    def presentToStrawerryType(self) -> list[BankAccountType]:
        return [BankAccountType(id=it.id,
        name=it.name,
        bank_name=it.bank_name,
        account_type=it.account_type,
        balance=it.balance,
        created_at=it.created_at,
        updated_at=it.updated_at,
        deleted_at=it.deleted_at) for it in self.data]
