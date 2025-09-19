from django.contrib import admin
from .models import Account, Transaction

# Register Account with a custom ModelAdmin
@admin.register(Account)
class AccountMod(admin.ModelAdmin):
    list_display = ('name', 'account_type', 'created_at', 'owner', 'deleted_at')
    list_filter = ('account_type', 'deleted_at')

@admin.register(Transaction)
class TransactionMod(admin.ModelAdmin):
    list_display = ("date", "debit_account", "credit_account", "gross_amount", "currency", "is_deleted", "created_at", "created_by",)
    list_filter = ("currency", "date", "deleted_at")
    search_fields = ("description", "debit_account__name", "credit_account__name")
    readonly_fields = ("created_at", "created_by", "deleted_at", "deleted_by")

    def get_queryset(self, request):
        return super().get_queryset(request).select_related("debit_account", "credit_account", "created_by", "deleted_by")

    def has_delete_permission(self, request, obj=None):
        return False