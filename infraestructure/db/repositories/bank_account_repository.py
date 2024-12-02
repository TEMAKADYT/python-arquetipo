from core.entities.bank_account_entity import BankAccountEntity
from infraestructure.models.bank_account_model import BankAccountModel
from infraestructure.db.builders.bank_account_builder import bankAccountFromModel
from infraestructure.db.builders.bank_account_builder import bankAccountsFromQuerySet

class BankAccountRepository:

    async def add(self, bank_account: BankAccountEntity) -> BankAccountEntity | None:
        try:
            model = await BankAccountModel(
                name=bank_account.name,
                bank_name=bank_account.bank_name,
                account_type=bank_account.account_type,
                balance=bank_account.balance
            )
            await model.save()
            return bankAccountFromModel(model)
        except Exception as e:
            print(f"Error during BankAccountRepository save: {e}")

    async def get_list(self):
        try:
            objects = await BankAccountModel.objects.all()
            return bankAccountsFromQuerySet(objects)
        except Exception as e:
            print("ERROR GETTING BANK ACCOUNTS")
            print(e)
            return []

    async def get_one_by_id(self, bank_account_id: int) -> BankAccountEntity:
        record = await BankAccountModel.objects.get(id=bank_account_id)
        return bankAccountFromModel(record)

    async def update(self, updated_entity: BankAccountEntity) -> BankAccountEntity:
        record = await BankAccountModel.objects.get(id=updated_entity.id)
        record.name = updated_entity.name
        record.bank_name = updated_entity.bank_name
        record.account_type = updated_entity.account_type
        record.balance = updated_entity.balance
        await record.save()
        return bankAccountFromModel(record)

    async def remove(self, bank_account_id: int) -> None:
        record = await BankAccountModel.objects.get(id=bank_account_id)
        await record.soft_delete()

    async def restore(self, bank_account_id: int) -> None:
        record = await BankAccountModel.objects.get(id=bank_account_id)
        return await record.restore()
