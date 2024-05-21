from django.shortcuts import render, HttpResponse
from .models import hotel
from .models import quarto
from .models import usuario
from .models import reserva
from .forms import FormReserva
from .forms import FormCadastro



# Create your views here.

def homepage(request):
    context = {}
    dados_hotel = hotel.objects.all
    context['dados_hotel'] = dados_hotel
    return render(request, 'homepage.html', context)

def quartos(request):
    context = {}
    tipos_quartos = ['SOLTEIRO', 'CASAL', 'COMFORT', 'LUXO']
    dados_quartos = []

    for tipo in tipos_quartos:
        quarto_tipo = quarto.objects.filter(tipo=tipo).first()
        if quarto_tipo:
            dados_quartos.append(quarto_tipo)

    context['dados_quarto'] = dados_quartos
    return render(request, 'quartos.html', context)

def quartos_solteiro(request):
    context = {}
    dados_quarto = quarto.objects.all()
    context['dados_quarto'] = dados_quarto
    return render(request, 'solteiro.html', context)

def quartos_casal(request):
    context = {}
    dados_quarto = quarto.objects.all()
    context['dados_quarto'] = dados_quarto
    return render(request, 'casal.html', context)

def quartos_comfort(request):
    context = {}
    dados_quarto = quarto.objects.all()
    context['dados_quarto'] = dados_quarto
    return render(request, 'comfort.html', context)

def quartos_luxo(request):
    context = {}
    dados_quarto = quarto.objects.all()
    context['dados_quarto'] = dados_quarto
    return render(request, 'luxo.html', context)

def cadastro(request):
    if request.method == "POST":
        form = FormCadastro(request.POST)
        if form.is_valid():
            var_first_name = form.cleaned_data['first_name']
            var_last_name = form.cleaned_data['last_name']
            var_user = form.cleaned_data['user']
            var_email = form.cleaned_data['email']
            var_senha = form.cleaned_data['senha']
        
            user = usuario.objects.create_user(username=var_user, email=var_email, senha=var_senha)
            user.first_name = var_first_name
            user.last_name = var_last_name
            user.save()
            
            return HttpResponse("<h1>Cadastrado com sucesso!</h1>")

    else:
        form = FormCadastro()

    return render(request, "cadastro.html", {"form": form})


def reservar(request):
    if request.method == "POST":
        form = FormReserva(request.POST)
        if form.is_valid():
            var_nome = form.cleaned_data['nome']
            var_email = form.cleaned_data['email']
            var_idade = form.cleaned_data['idade']
            var_data = form.cleaned_data['data']
            var_quarto = form.cleaned_data['quarto']

            reservar_quarto = reserva(nome=var_nome, email=var_email, idade=var_idade, data=var_data, quarto=var_quarto)
            reservar_quarto.save()

            return HttpResponse("<h1>Você realizou uma reserva!</h1>")

    else:
        form = FormReserva()

    return render(request, "reservar.html", {"form": form})
