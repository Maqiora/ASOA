from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Account
from .forms import AccountForm

def Account_list_and_create(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account_list')
        
def home(request):
    return render(request, 'home.html')
 
class AccountCreateView(CreateView):
    model = Account
    form_class = AccountForm
    template_name = 'ksiegowosc/account_list.html'
    success_url = reverse_lazy('account_list')

class AccountUpdateView(UpdateView):
    model = Account
    form_class = AccountForm
    template_name = 'ksiegowosc/account_list.html'
    success_url = reverse_lazy('account_list')

class AccountDeleteView(DeleteView):
    model = Account
    template_name = 'ksiegowosc/account_list.html'
    success_url = reverse_lazy('account_list')


