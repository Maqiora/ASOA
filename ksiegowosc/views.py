from django.views import View
from django.shortcuts import render, redirect
from django.views.generic.list import MultipleObjectMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Account
from .forms import AccountForm

class AccountListCreateView(View, MultipleObjectMixin):
    model = Account
    form_class = AccountForm
    template_name = 'ksiegowosc/account_list.html'
    context_object_name = 'accounts'

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        form = self.form_class()
        context = self.get_context_data(form=form)
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account_list')
        context = self.get_context_data(form=form)
        return render(request, self.template_name, context)
 
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


