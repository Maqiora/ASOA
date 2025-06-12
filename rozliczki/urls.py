from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib import admin
from ksiegowosc import views  # only needed if you use it somewhere

urlpatterns = [
    path('', RedirectView.as_view(url='/accounts/', permanent=False)),
    path('accounts/', include('ksiegowosc.urls')),
    path('admin/', admin.site.urls),
]

