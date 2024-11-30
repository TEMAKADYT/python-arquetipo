from tortoise.models import Model
from tortoise import fields
from .BaseModel import BaseModel

class BankAccountModel(BaseModel):
    name = fields.CharField(max_length=100, null=False)
    bank_name = fields.CharField(max_length=100, null=False)
    account_type = fields.CharField(max_length=10, null=False)
    balance = fields.FloatField(default=0.0)

    # Soft delete objects queryset
    # objects =

    def __str__(self):
            return f"{self.name} - {self.bank_name} - {self.account_type} - {self.balance}"

    class Meta(BaseModel.Meta):
        table = "bank_accounts"
        # Default ordering
        ordering = ["name"]
