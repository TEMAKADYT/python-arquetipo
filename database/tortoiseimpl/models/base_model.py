from tortoise import fields, models
from datetime import datetime
from database.tortoiseimpl.logical_delete_manager import WithLogicalDeleteManager
from tortoise.manager import Manager
from tortoise.models import Model

class BaseModel(models.Model):

    # Use an integer field as the primary key
    id = fields.IntField(pk=True)

    # Use an UUID field as the primary key
    # id = fields.UUIDField(pk=True)

    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    deleted_at = fields.DatetimeField(null=True, default=None)  # Soft delete field

    # Can search from the deleted records
    with_deleted = Manager()
    objects = WithLogicalDeleteManager()

    class Meta(Model.Meta):
        abstract = True

        # Ignore Soft Deleted records

        # Example of indexes
        # indexes = [
        #            FullTextIndex(fields={"full_text"}, parser_name="ngram"),
        #            SpatialIndex(fields={"geometry"}),
        #        ]

    async def soft_delete(self) -> None:
        """
        Soft delete the record by setting the deleted_at field to the current timestamp.
        """
        self.deleted_at = datetime.utcnow()
        return await self.save()

    async def restore(self) -> None:
        """
        Restore a soft-deleted record by setting deleted_at to None.
        """
        self.deleted_at = None
        return await self.save()
