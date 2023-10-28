from django.db import models

# Create your models here.

class Burger(models.Model):
    immagine = models.ImageField()
    nome = models.CharField(max_length=20)
    prezzo = models.FloatField()
    descrizione = models.CharField(max_length=800)

    def __str__(self):
        return self.nome