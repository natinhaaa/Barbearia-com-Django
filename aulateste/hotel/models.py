from django.db import models
from django.utils import timezone

# Create your models here.

TIPOS_QUARTOS = (
    ("SOLTEIRO", "Solteiro"),
    ("CASAL", "Casal"),
    ("COMFORT", "Comfort"),
    ("LUXO", "Luxo")
)


class hotel(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=500)
    foto_hotel = models.ImageField(upload_to="Foto_Hotel/")

    def __str__(self):
        return self.titulo

class quarto(models.Model):
    tipo = models.CharField(max_length=15, choices=TIPOS_QUARTOS)
    disponibilidade= models.IntegerField()
    valor = models.FloatField(max_length=4)
    descricao = models.TextField(max_length=230)
    foto_quarto = models.ImageField(upload_to="Foto_Quarto/")

    def __str__(self):
        return self.tipo

class reserva(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField(max_length=20)
    idade = models.IntegerField()
    data = models.DateField(default=timezone.now)
    quarto = models.CharField(max_length=50)
