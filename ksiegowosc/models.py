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

class Transaction(models.Model):
    """Represents a financial transaction."""

    # Core fields
    date = models.DateField()
    debit_account = models.ForeignKey(
        Account,
        on_delete=models.PROTECT,
        related_name="debit_transactions"
    )
    credit_account = models.ForeignKey(
        Account,
        on_delete=models.PROTECT,
        related_name="credit_transactions"
    )
    description = models.TextField(blank=True)

    net_amount = models.DecimalField(max_digits=12, decimal_places=2)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    gross_amount = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=3)  # ISO 4217 code (e.g. "USD", "EUR")

    # Debugging / auditing fields
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_transactions"
    )
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="deleted_transactions"
    )

    class Meta:
        ordering = ["-date", "-created_at"]

    def __str__(self):
        return f"{self.date} | {self.debit_account} -> {self.credit_account} | {self.gross_amount} {self.currency}"