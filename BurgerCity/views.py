from django.shortcuts import render
from .models import Burger
# Create your views here.

def BurgerCity(request):
    Burgers = Burger.objects.all()
    return render(request, 'BurgerCity/burgercity.html', {'Burgers': Burgers})

def contattaci(request):
    return render(request, 'BurgerCity/contattaci.html')