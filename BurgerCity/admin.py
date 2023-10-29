from django.contrib import admin
from .models import Burger
from .models import contactForm

# Register your models here.

admin.site.register(Burger)
admin.site.register(contactForm)
