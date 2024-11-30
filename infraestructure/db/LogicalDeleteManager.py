from tortoise.manager import Manager

class WithLogicalDeleteManager(Manager):
    """Include this manager in a model to get all information without deleted records"""

    def get_queryset(self):
        return super(WithLogicalDeleteManager, self).get_queryset().filter(deleted_at__isnull=True)
