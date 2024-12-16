from database.repositories.transaction_repository import TransactionRepository
from application.interactors.transaction_interactors import TransactionInteractors
from web.graphql.types.types import TransactionType
from application.presenters.transaction_presenters import TransactionPresenter

from dependency_injector.wiring import Provide, inject
from web.web_container import WebContainerDI
from domain.entities.transaction_entity import TransactionEntity
from application.presenters.transaction_presenters import TransactionListPresenter

@inject
def get_repository(repository_impl : TransactionRepository = Provide[WebContainerDI.transaction_repository]):
    return repository_impl

@inject
def get_interactor(interactor_impl : TransactionInteractors = Provide[WebContainerDI.transaction_interactor]):
    return interactor_impl

async def get_transaction_by_id(entity_id: int) -> TransactionType:
    interactor = get_interactor()
    # Execution
    result = await interactor.get_transaction_by_id(entity_id)
    # Presenter
    gql_presenter = TransactionPresenter(result)
    return gql_presenter.presentToStrawerryType()

async def get_transactions() -> list[TransactionType]:
    interactor = get_interactor()
    # Execution
    result = await interactor.get_transactions()
    # Presenter
    gql_presenter = TransactionListPresenter(data=result)
    return gql_presenter.presentToStrawerryType()

async def create_transaction(entity : TransactionEntity) -> TransactionType:
    interactor = get_interactor()
    # Execution
    result = await interactor.create_transaction(entity)
    # Presenter
    gql_presenter = TransactionPresenter(result)
    return gql_presenter.presentToStrawerryType()

async def update_transaction(entity : TransactionEntity) -> TransactionType:
    interactor = get_interactor()
    # Execution
    record = await interactor.update_transaction(entity)
    # Presenter
    gql_presenter = TransactionPresenter(record)
    return gql_presenter.presentToStrawerryType()

async def remove_transaction(entity_id : int):
    interactor = get_interactor()
    # Execution
    await interactor.remove_transaction(entity_id)
    # NOT RETURN
