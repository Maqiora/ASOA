from django.urls import path 
<<<<<<< HEAD
from .views import (
    AccountListView,
    AccountCreateView,
    AccountUpdateView,
    AccountDeleteView,
)

urlpatterns = [
    path('', AccountListView.as_view(), name='account_list'),  
    path('create/', AccountCreateView.as_view(), name='account_create'),
    path('<int:pk>/edit/', AccountUpdateView.as_view(), name='account_edit'),
    path('<int:pk>/delete/', AccountDeleteView.as_view(), name='account_delete'),
]
=======
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("wydatki/", views.wydatki, name="wydatki")
]
>>>>>>> 8702e905c9eb88b49bca0485c8db1f00fd1d7221
