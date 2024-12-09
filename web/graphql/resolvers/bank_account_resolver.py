from database.repositories.bank_account_repository import BankAccountRepository
from application.interactors.bank_account_interactors import BankAccountInteractors
from domain.entities.bank_account_entity import BankAccountEntity
from application.presenters.bank_account_presenters import BankAccountPresenter
from web.graphql.types.types import BankAccountType
from application.presenters.bank_account_presenters import BankAccountListPresenter

async def get_bankaccount_by_id(entity_id: int) -> BankAccountType:
    # Repository
    repository_impl = BankAccountRepository()
    # Interactor
    interactor = BankAccountInteractors(repository_impl)
    # Execution
    result = await interactor.get_bankaccount_by_id(entity_id)
    # Presenter
    gql_presenter = BankAccountPresenter(result)
    return gql_presenter.presentToStrawerryType()

async def get_bank_accounts() -> list[BankAccountType]:
    # Repository
    repository_impl = BankAccountRepository()
    # Interactor
    interactor = BankAccountInteractors(repository_impl)
    # Execution
    result = await interactor.get_bank_accounts()
    # Presenter
    gql_presenter = BankAccountListPresenter(data=result)
    return gql_presenter.presentToStrawerryType()

async def create_bank_account(entity : BankAccountEntity) -> BankAccountType:
    # Repository
    repository_impl = BankAccountRepository()
    # Interactor
    interactor = BankAccountInteractors(repository_impl)
    # Execution
    result = await interactor.create_bank_account(entity)
    # Presenter
    gql_presenter = BankAccountPresenter(result)
    return gql_presenter.presentToStrawerryType()

async def update_bank_account(entity : BankAccountEntity) -> BankAccountType:
    # Repository
    repository_impl = BankAccountRepository()
    # Interactor
    interactor = BankAccountInteractors(repository_impl)
    # Execution
    record = await interactor.update_bank_account(entity)
    # Presenter
    gql_presenter = BankAccountPresenter(record)
    return gql_presenter.presentToStrawerryType()

async def remove_bank_account(entity_id : int):
    # Repository
    repository_impl = BankAccountRepository()
    # Interactor
    interactor = BankAccountInteractors(repository_impl)
    # Execution
    await interactor.remove_bank_account(entity_id)
    # NOT RETURN
