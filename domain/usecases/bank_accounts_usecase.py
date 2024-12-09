from domain.entities.bank_account_entity import BankAccountEntity
from domain.usecases.crud_base_usecase import UpdateUsecase
from domain.usecases.crud_base_usecase import DeleteUsecase
from domain.usecases.crud_base_usecase import CreateUsecase
from domain.usecases.crud_base_usecase import ListUsecase
from domain.usecases.crud_base_usecase import FindOneByIdUsecase

# Basic CRUD For BankAccountEntity
class FindOneBankAccountByIdUsecase(FindOneByIdUsecase[BankAccountEntity]):
    pass

class ListBankAccountsUsecase(ListUsecase[BankAccountEntity]):
    pass

class CreateAccountUsecase(CreateUsecase[BankAccountEntity]):
    pass

class DeleteAccountUsecase(DeleteUsecase[BankAccountEntity]):
    pass

class UpdateBankAccountUsecase(UpdateUsecase[BankAccountEntity]):
    pass
