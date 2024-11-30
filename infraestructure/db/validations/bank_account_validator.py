from origamiapp.infraestructure.models import BankAccountModel
from tortoise import fields
from tortoise.validators import MaxLengthValidator

class BankAccountValidatorModel(BankAccountModel):
    name = fields.CharField(validators=[MaxLengthValidator(100)])
