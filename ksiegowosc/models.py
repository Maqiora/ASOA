from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class ActiveMod(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)

class Account(models.Model):
    ACCOUNT_TYPES = (
        ('internal', 'Internal'),
        ('external', 'External'),
    )

    name = models.CharField(max_length=300)
    account_type = models.CharField(max_length=250, choices=ACCOUNT_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)

    objects = models.Manager()  # default mod includes the banished
    active = ActiveMod()        # custom mod excludes the banished

    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def is_deleted(self):
        return self.deleted_at is not None

    def __str__(self):
        return self.name

# class Transaction(models.Mode):
#     date = models.DateTimeField(auto_now_add=True)
#     debit_bucket = models.IntegerField()
#     credit_bucket = models.IntegerField()
#     description = models.CharField(max_length=250)
#     net_amount = models.IntegerField()
#     tax_amount = models.IntegerField()
#     gross_amount = models.IntegerField()
#     currency = models.Choices()



# Johny's Issue's
# Allow entering transactions.
# A transaction has:
# a date
# debit account
# credit account
# description
# net amount
# tax amount
# gross amount
# currency
# For debugging, we can additionally record:
# the creation date and time,
# the user who created the transaction,
# the date and time when the transaction was (soft) deleted