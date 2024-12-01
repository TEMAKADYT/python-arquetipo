from tortoise import fields
from .base_model import BaseModel

class TransactionModel(BaseModel):
    amount = fields.FloatField(null=False)
    type = fields.CharField(max_length=10, null=False)
    account = fields.CharField(max_length=10, null=True)
    subaccount = fields.CharField(max_length=60, null=True)
    taxable = fields.BooleanField(default=False)
    description = fields.TextField(null=True)
    date = fields.DatetimeField()

    # Relaionships
    bank_account = fields.ForeignKeyField("models.BankAccountModel", related_name="transactions")

    def __str__(self):
        # interpolate princial fields
        return f"{self.type} - {self.description} - {self.amount}"

    class Meta:
        table = "transactions"
        ordering = ["date"]
