from django.shortcuts import render
<<<<<<< HEAD
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

=======
from .models import wydatki

# Create your views here.

def home(request): 
    return render(request, "home.html")

def wydatki(request):
    items = wydatki.objects.all()
    return render(request, "wydatki.html", {"wydatki" : items})
>>>>>>> 8702e905c9eb88b49bca0485c8db1f00fd1d7221
