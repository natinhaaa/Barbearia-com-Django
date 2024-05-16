from django.db import models

# Create your models here.

TIPOS_QUARTOS = (
    ("SOLTEIRO", "Solteiro"),
    ("CASAL", "Casal"),
    ("COMFORT", "Comfort"),
    ("LUXO", "Luxo")
)

NOME_QUARTOS = (
    ("SOLTEIRO CONFORTÁVEL", "Solteiro Confortável"),
    ("SOLTEIRO COM VISTA", "Solteiro com Vista"),
    ("SOLTEIRO ECONÔMICO", "Solteiro Econômico"),
    ("CASAL LUXO", "Casal Luxo"),
    ("SUÍTE ROMÂNTICA", "Suíte Romântica"),
    ("CASAL STANDARD", "Casal Standard"),
    ("SUPERIOR COM VISTA", "Superior com Vista"),
    ("COMFORT CLÁSSICO", "Comfort Clássico"),
    ("COMFORT DELUXE", "Comfort Deluxe"),
    ("COMFORT EXECUTIVO", "Comfort Executivo"),
    ("COMFORT FAMILIAR", "Comfort Familiar"),
    ("SUÍTE LUXO EXECUTIVO", "Suíte Luxo Executivo"),
    ("SUÍTE PRESIDENCIAL", "Suíte Presidencial"),
    ("LUXO PREMIUM", "Luxo Premium"),
    ("SUÍTE REAL", "Suíte Real"),
)

class hotel(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=500)
    foto_hotel = models.ImageField(upload_to="Foto_Hotel/")

    def __str__(self):
        return self.titulo

class quarto(models.Model):
    tipo = models.CharField(max_length=15, choices=TIPOS_QUARTOS)
    nome = models.CharField(max_length=20, choices=NOME_QUARTOS)
    disponibilidade= models.IntegerField()
    valor = models.FloatField(max_length=4)
    descricao = models.TextField(max_length=230)
    foto_quarto = models.ImageField(upload_to="Foto_Quarto/")

    def __str__(self):
        return self.tipo
    
class usuario(models.Model):
    nome = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    senha = models.CharField(max_length=20)

    def __str__ (self):
        return self.nome