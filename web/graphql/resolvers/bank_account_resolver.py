from database.repositories.bank_account_repository import BankAccountRepository
from application.interactors.bank_account_interactors import BankAccountInteractors
from domain.entities.bank_account_entity import BankAccountEntity
from application.presenters.bank_account_presenters import BankAccountPresenter
from web.graphql.types.types import BankAccountType
from application.presenters.bank_account_presenters import BankAccountListPresenter
from dependency_injector.wiring import Provide, inject
from web.web_container import WebContainerDI

@inject
def get_repository(repository_impl : BankAccountRepository = Provide[WebContainerDI.bank_account_repository]):
    return repository_impl

@inject
def get_interactor(interactor_impl : BankAccountInteractors = Provide[WebContainerDI.bank_account_interactor]):
    return interactor_impl

async def get_bankaccount_by_id(entity_id: int) -> BankAccountType:
    interactor = get_interactor()
    # Execution
    result = await interactor.get_bankaccount_by_id(entity_id)
    # Presenter
    gql_presenter = BankAccountPresenter(result)
    return gql_presenter.presentToStrawerryType()

async def get_bank_accounts() -> list[BankAccountType]:
    interactor = get_interactor()
    # Execution
    result = await interactor.get_bank_accounts()
    # Presenter
    gql_presenter = BankAccountListPresenter(data=result)
    return gql_presenter.presentToStrawerryType()

async def create_bank_account(entity : BankAccountEntity) -> BankAccountType:
    interactor = get_interactor()
    # Execution
    result = await interactor.create_bank_account(entity)
    # Presenter
    gql_presenter = BankAccountPresenter(result)
    return gql_presenter.presentToStrawerryType()

async def update_bank_account(entity : BankAccountEntity) -> BankAccountType:
    interactor = get_interactor()
    # Execution
    record = await interactor.update_bank_account(entity)
    # Presenter
    gql_presenter = BankAccountPresenter(record)
    return gql_presenter.presentToStrawerryType()

async def remove_bank_account(entity_id : int):
    interactor = get_interactor()
    # Execution
    await interactor.remove_bank_account(entity_id)
    # NOT RETURN
