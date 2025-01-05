from domain.entities.bank_account_entity import BankAccountEntity
from database.builders.bank_account_builder import bankAccountFromModel
from database.builders.bank_account_builder import bankAccountsFromQuerySet
from domain.repositories.crud_repository_interface import CRUDRepositoryInterface
from database.tortoiseimpl.models import BankAccountModel

class BankAccountRepository(CRUDRepositoryInterface):

    async def create(self, entity: BankAccountEntity) -> BankAccountEntity | None:
        try:
            model = await BankAccountModel(
                name=entity.name,
                bank_name=entity.bank_name,
                account_type=entity.account_type,
                balance=entity.balance,
                color=entity.color
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

    async def get_one_by_id(self, id: int | str) -> BankAccountEntity:
        record = await BankAccountModel.objects.get(id=id)
        return bankAccountFromModel(record)

    async def update(self, entity: BankAccountEntity) -> BankAccountEntity:
        record = await BankAccountModel.objects.get(id=entity.id)
        record.name = entity.name
        record.bank_name = entity.bank_name
        record.account_type = entity.account_type
        record.balance = entity.balance
        record.color = entity.color
        await record.save()
        return bankAccountFromModel(record)

    async def remove(self, id: int | str) -> None:
        record = await BankAccountModel.objects.get(id=id)
        await record.soft_delete()

    async def restore(self, id: int | str) -> None:
        record = await BankAccountModel.objects.get(id=id)
        return await record.restore()
