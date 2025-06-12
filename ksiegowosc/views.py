from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Account
from .forms import AccountForm

def home(request):
    return render(request, 'home.html')

class AccountListView(ListView):
    model = Account
    template_name = 'account_list.html'
    context_object_name = 'accounts'
    
    def get_queryset(self):
        return Account.active.all()
    
class AccountCreateView(CreateView):
    model = Account
    form_class = AccountForm
    template_name = 'account_list.html'
    success_url = reverse_lazy('account_list')

class AccountUpdateView(UpdateView):
    model = Account
    form_class = AccountForm
    template_name = 'account_list.html'
    success_url = reverse_lazy('account_list')

class AccountDeleteView(DeleteView):
    model = Account
    template_name = 'account_list.html'
    success_url = reverse_lazy('account_list')


