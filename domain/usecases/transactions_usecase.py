from domain.entities.transaction_entity import TransactionEntity
from domain.usecases.crud_base_usecase import UpdateUsecase
from domain.usecases.crud_base_usecase import DeleteUsecase
from domain.usecases.crud_base_usecase import CreateUsecase
from domain.usecases.crud_base_usecase import ListUsecase
from domain.usecases.crud_base_usecase import FindOneByIdUsecase

# Basic CRUD For TransactionEntity
class FindOneTransactionByIdUsecase(FindOneByIdUsecase[TransactionEntity]):
    pass

class ListTransactionsUsecase(ListUsecase[TransactionEntity]):
    pass

class CreateAccountUsecase(CreateUsecase[TransactionEntity]):
    pass

class DeleteAccountUsecase(DeleteUsecase[TransactionEntity]):
    pass

class UpdateTransactionUsecase(UpdateUsecase[TransactionEntity]):
    pass
