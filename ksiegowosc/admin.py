from django.contrib import admin
from .models import Account

# Register your models here.

admin.register(Account)
class AccountMod(admin.ModelAdmin):
    list_display = ('name', 'account_type', 'created_at', 'owner', 'deleted_at')
    list_filter = ('account_type', 'deleted_at')
   