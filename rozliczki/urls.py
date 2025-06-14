from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib import admin

urlpatterns = [
    path('', RedirectView.as_view(url='/accounts/', permanent=False)),
    path('accounts/', include('ksiegowosc.urls')),
    path('admin/', admin.site.urls),
]

