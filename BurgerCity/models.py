from django.db import models

# Create your models here.


class contactForm(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    userQuestion = models.CharField(max_length=800)

    def __str__(self):
        return self.email


class Burger(models.Model):
    immagine = models.ImageField()
    nome = models.CharField(max_length=20)
    prezzo = models.FloatField()
    descrizione = models.CharField(max_length=800)

    def __str__(self):
        return self.nome
