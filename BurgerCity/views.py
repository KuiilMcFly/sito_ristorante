from django.shortcuts import render, redirect
from .models import Burger
from .models import contactForm
from .forms import ContactFormForm

# Create your views here.


def BurgerCity(request):
    Burgers = Burger.objects.all()
    return render(request, 'BurgerCity/burgercity.html', {'Burgers': Burgers})


def contattaci(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contattaci')
    else:
        form = ContactFormForm()

    data = contactForm.objects.all()
    return render(request, 'BurgerCity/contattaci.html', {'form': form, 'data': data})
