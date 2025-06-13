from django.urls import path
from . import views
from .views import (
    AccountCreateView,
    AccountUpdateView,
    AccountDeleteView,
    Account_list_and_create
)

urlpatterns = [
    path('accounts/', Account_list_and_create.as_view, name='account_add'),
    path('create/', AccountCreateView.as_view(), name='account_create'),
    path('<int:pk>/edit/', AccountUpdateView.as_view(), name='account_edit'),
    path('<int:pk>/delete/', AccountDeleteView.as_view(), name='account_delete'),
]