from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Account, Transaction
from .forms import AccountForm, TransactionForm
 

class DashboardView(TemplateView):
    template_name = "ksiegowosc/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["accounts"] = Account.active.all()
        context["transactions"] = Transaction.active.all()
        context["account_form"] = AccountForm()
        context["transaction_form"] = TransactionForm()
        return context

    def post(self, request, *args, **kwargs):
        if "account_submit" in request.POST:
            form = AccountForm(request.POST)
            if form.is_valid():
                form.save(user=request.user)   
                return redirect("dashboard")
            context = self.get_context_data()
            context["account_form"] = form
            return self.render_to_response(context)
        
        elif "transaction_submit" in request.POST:
            form = TransactionForm(request.POST)
            if form.is_valid():
                form.save()   # ✅ no user kwarg
                return redirect("dashboard")
            context = self.get_context_data()
            context["transaction_form"] = form
            return self.render_to_response(context)

class AccountUpdateView(UpdateView):
    model = Account
    form_class = AccountForm
    template_name = "ksiegowosc/account_form.html"
    success_url = reverse_lazy("dashboard")

    def get_queryset(self):
        return Account.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = AccountForm()
        return context

    def post(self, request, *args, **kwargs):
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        context = self.get_context_data(form=form)
        return self.render_to_response(context)


class AccountDeleteView(DeleteView):
    model = Account
    template_name = "ksiegowosc/account_delete.html"
    success_url = reverse_lazy("dashboard")

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.soft_delete()
        return redirect(self.success_url)

class ExpenseView(TemplateView):
    template_name = "ksiegowosc/expenses.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["expenses"] = Transaction.active.all()
        context["form"] = TransactionForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save(user=request.user)
            return redirect("expenses")
        context = self.get_context_data()
        context["form"] = form
        return self.render_to_response(context)
        