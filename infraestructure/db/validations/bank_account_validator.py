from infraestructure.models.bank_account_model import BankAccountModel
from tortoise import fields
from tortoise.validators import MaxLengthValidator

class BankAccountValidatorModel(BankAccountModel):
    pass
    # TODO
    # name = fields.CharField(validators=[MaxLengthValidator(100)])
