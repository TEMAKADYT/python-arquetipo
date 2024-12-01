from tortoise import fields
from .base_model import BaseModel
from tortoise import models
from tortoise.models import Model

class BankAccountModel(BaseModel):
    name = fields.CharField(max_length=100, null=False)
    bank_name = fields.CharField(max_length=100, null=False)
    account_type = fields.CharField(max_length=10, null=False)
    balance = fields.FloatField(default=0.0)

    def __str__(self):
        return f"{self.name} - {self.bank_name} - {self.account_type} - {self.balance}"

    class Meta:
        table = "bank_accounts"
        # Default ordering
        # ordering = ["name"]
