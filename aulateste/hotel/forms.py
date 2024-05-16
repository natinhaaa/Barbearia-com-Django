from django import forms

class FormNome(forms.Form):
    nome = forms.CharField(label="Nome", max_length=20)
    email= forms.EmailField(label="E-mail", max_length=20)
    senha= forms.CharField(label="Senha", max_length=20, widget=forms.PasswordInput)