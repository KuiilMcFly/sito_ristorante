from django.urls import path
from . import views

urlpatterns = [
    path('', views.BurgerCity, name='BurgerCity'),
    path('contattaci', views.contattaci, name='contattaci'),
]
