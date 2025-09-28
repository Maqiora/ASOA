from django import forms
from .models import Account, Transaction

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['name', 'account_type', 'owner']
        
    def save(self, commit=True, user=None):  
        instance = super().save(commit=False)
        if user and not instance.owner:
            instance.owner = user
        if commit:
            instance.save()
        return instance


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = [
            'date',
            'description',
            'debit_account',
            'credit_account',
            'net_amount',
            'tax_amount',
            'currency',
        ]

    def save(self, commit=True):
        instance = super().save(commit=False)
        if instance.net_amount is not None and instance.tax_amount is not None:
            instance.gross_amount = instance.net_amount + instance.tax_amount
        if commit:
            instance.save()
        return instance