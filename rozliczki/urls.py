from django.contrib import admin
from django.urls import path, include
from ksiegowosc import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("ksiegowosc.urls"))
]


