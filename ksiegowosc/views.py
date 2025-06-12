from django.shortcuts import render
from .models import wydatki

# Create your views here.

def home(request): 
    return render(request, "home.html")

def wydatki(request):
    items = wydatki.objects.all()
    return render(request, "wydatki.html", {"wydatki" : items})