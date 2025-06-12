from django.contrib import admin
<<<<<<< HEAD
from .models import Account

# Register your models here.

admin.register(Account)
class AccountMod(admin.ModelAdmin):
    list_display = ('name', 'account_type', 'created_at', 'owner', 'deleted_at')
    list_filter = ('account_type', 'deleted_at')
   
=======
from .models import wydatki

# Register your models here.

admin.site.register(wydatki)
>>>>>>> 8702e905c9eb88b49bca0485c8db1f00fd1d7221
