from django.urls import path
from .views import DashboardView, AccountUpdateView, AccountDeleteView

urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
    path("account/<int:pk>/edit/", AccountUpdateView.as_view(), name="account_edit"),
    path("account/<int:pk>/delete/", AccountDeleteView.as_view(), name="account_delete"),
]
