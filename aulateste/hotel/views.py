from django.shortcuts import render, HttpResponse
from .models import hotel
from .models import quarto


# Create your views here.

def homepage(request):
    context = {}
    dados_hotel = hotel.objects.all
    context['dados_hotel'] = dados_hotel
    return render(request, 'homepage.html', context)

def reserve(request):
    context = {}
    dados_quarto = quarto.objects.all()
    context['dados_quarto'] = dados_quarto
    return render(request, 'reserve.html', context) #retorna a pagina quartos.html

