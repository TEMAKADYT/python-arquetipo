from origamiapp.core.entities.BankAccount import BankAccount
from origamiapp.infraestructure.models.BankAccountModel import BankAccountModel
from origamiapp.infraestructure.db.validations.bank_account_validator import BankAccountValidatorModel
from origamiapp.infraestructure.db.builders.BankAccountBuilder import bankAccountFromModel
from origamiapp.infraestructure.db.builders.BankAccountBuilder import bankAccountsFromQuerySet

class BankAccountRepository:

    async def add(self, bank_account: BankAccount) -> BankAccount:

        # Validate Payload Data
        await BankAccountValidatorModel.create(name = bank_account.name)

        # Persist Data
        new_record = BankAccountModel.create(
            name = bank_account.name,
            bank_name = bank_account.bank_name,
            account_type = bank_account.account_type,
            balance = bank_account.balance,
        )

        return bankAccountFromModel(new_record)

    async def get_list(self):
        all = bankAccountsFromQuerySet(BankAccountModel.all())
        return all

    async def get_by_id(self, bank_account_id: int) -> BankAccount:
        record = BankAccountModel.get(id=bank_account_id)
        return bankAccountFromModel(record)

    async def remove(self, bank_account_id: int) -> None:
        return BankAccountModel.get(id=bank_account_id).soft_delete()

    async def restore(self, bank_account_id: int) -> None:
        return BankAccountModel.get(id=bank_account_id).restore()
