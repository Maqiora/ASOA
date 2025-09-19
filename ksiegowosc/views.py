from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Account, Transaction
from .forms import AccountForm


class DashboardView(TemplateView):
    template_name = "ksiegowosc/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["accounts"] = Account.active.all()
        context["transactions"] = Transaction.active.all()
        context["form"] = AccountForm()
        return context

    def post(self, request, *args, **kwargs):
        """Handle Account form submission directly on the dashboard."""
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
        context = self.get_context_data()
        context["form"] = form
        return self.render_to_response(context)


class AccountUpdateView(UpdateView):
    model = Account
    form_class = AccountForm
    template_name = "ksiegowosc/account_form.html"
    success_url = reverse_lazy("dashboard")


class AccountDeleteView(DeleteView):
    model = Account
    template_name = "ksiegowosc/account_confirm_delete.html"
    success_url = reverse_lazy("dashboard")

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.soft_delete()
        return redirect(self.success_url)
