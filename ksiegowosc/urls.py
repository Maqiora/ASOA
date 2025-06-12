from django.urls import path
from . import views
from .views import (
    AccountListView,
    AccountCreateView,
    AccountUpdateView,
    AccountDeleteView,
)

urlpatterns = [
    path("", views.home, name="home"),
    path("wydatki/", views.wydatki, name="wydatki"),
    path('', AccountListView.as_view(), name='account_list'),
    path('create/', AccountCreateView.as_view(), name='account_create'),
    path('<int:pk>/edit/', AccountUpdateView.as_view(), name='account_edit'),
    path('<int:pk>/delete/', AccountDeleteView.as_view(), name='account_delete'),
]