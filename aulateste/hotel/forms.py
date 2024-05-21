from django import forms
from .models import quarto

class FormReserva(forms.Form):
    nome = forms.CharField(label='Nome', max_length=30)
    email = forms.EmailField(label='E-mail', max_length=50)
    idade = forms.IntegerField(label='Idade')
    data = forms.DateField(label='Data', widget=forms.DateInput(attrs={'type': 'date'}))
    quarto = forms.ModelChoiceField(label='Quarto', queryset=quarto.objects.filter(id__in=[3, 4, 5, 6]))

    
class FormCadastro(forms.Form):
    first_name = forms.CharField(label="Nome:", max_length=20)
    last_name = forms.CharField(label="Sobrenome:", max_length=20)
    user = forms.CharField(label="Usuário:", max_length=20)
    email = forms.EmailField(label="E-mail:", max_length=100)
    password = forms.CharField(label="Senha:", widget=forms.PasswordInput)

class FormLogin(forms.Form):
    user = forms.CharField(label="Usuário:", max_length=20)
    password = forms.CharField(label="Senha:", widget=forms.PasswordInput)