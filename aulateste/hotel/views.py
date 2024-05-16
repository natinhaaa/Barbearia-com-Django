from django.shortcuts import render, HttpResponse
from .models import hotel
from .models import quarto
from .models import usuario
from .forms import FormNome


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
    return render(request, 'reserva_quarto.html', context) #retorna a pagina quartos.html

def reserva_solteiro(request):
    context = {}
    dados_quarto = quarto.objects.all()
    context['dados_quarto'] = dados_quarto
    return render(request, 'solteiro.html', context)

def reserva_casal(request):
    context = {}
    dados_quarto = quarto.objects.all()
    context['dados_quarto'] = dados_quarto
    return render(request, 'casal.html', context)

def reserva_comfort(request):
    context = {}
    dados_quarto = quarto.objects.all()
    context['dados_quarto'] = dados_quarto
    return render(request, 'comfort.html', context)

def reserva_luxo(request):
    context = {}
    dados_quarto = quarto.objects.all()
    context['dados_quarto'] = dados_quarto
    return render(request, 'luxo.html', context)

def nome(request):
    if request.method == "POST":
        form = FormNome(request.POST)
        if form.is_valid():
            var_nome = form.cleaned_data['nome']
            var_email = form.cleaned_data['email']
            var_senha = form.cleaned_data['senha']

            user = usuario(nome=var_nome, email=var_email, senha= var_senha)
            user.save()

            print(var_email, var_nome, var_senha)

            return HttpResponse("<h1>Você foi cadastrado.</h1>")

    else:
        form = FormNome()

    return render(request, "nome.html", {"form": form})