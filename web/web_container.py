from dependency_injector import containers, providers
from database.repositories.bank_account_repository import BankAccountRepository
from application.interactors.bank_account_interactors import BankAccountInteractors

class WebContainerDI(containers.DeclarativeContainer):

    # config = providers.Configuration(ini_files=["config.ini"])
    # wiring_config = containers.WiringConfiguration(
    #     modules=["web"],
    #     packages=['web']
    # )

    # Gateways

    # database_client = providers.Singleton(
    #     sqlite3.connect,
    #     config.database.dsn,
    # )

    # Repositories
    bank_account_repository = providers.Factory(
        BankAccountRepository,
    )

    # Interactors
    bank_account_interactor = providers.Factory(
        BankAccountInteractors,
        bank_account_repository=bank_account_repository,
    )
