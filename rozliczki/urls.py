<<<<<<< HEAD
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib import admin

urlpatterns = [
    path('', RedirectView.as_view(url='/accounts/', permanent=False)),  # redirect homepage to accounts
    path('accounts/', include('ksiegowosc.urls')),
    path('admin/', admin.site.urls),
]
=======
from django.contrib import admin
from django.urls import path, include
from ksiegowosc import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("ksiegowosc.urls"))
]


>>>>>>> 8702e905c9eb88b49bca0485c8db1f00fd1d7221
