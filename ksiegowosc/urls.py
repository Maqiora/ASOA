from django.urls import path
from . import views
from .views import (
    AccountCreateView,
    AccountUpdateView,
    AccountDeleteView,
    AccountListCreateView
)

urlpatterns = [
    path('', AccountListCreateView.as_view(), name='account_list'),
    path('create/', AccountCreateView.as_view(), name='account_create'),
    path('<int:pk>/edit/', AccountUpdateView.as_view(), name='account_edit'),
    path('<int:pk>/delete/', AccountDeleteView.as_view(), name='account_delete'),
]