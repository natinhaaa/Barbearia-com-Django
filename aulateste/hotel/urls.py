from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('reserva', views.reserve, name='reserva'),
    path('reserva_solteiro', views.reserva_solteiro, name='reserva_solteiro'),
    path('reserva_casal', views.reserva_casal, name='reserva_casal'),
    path('reserva_comfort', views.reserva_comfort, name='reserva_comfort'),
    path('reserva_luxo', views.reserva_luxo, name='reserva_luxo'),
    path('nome', views.nome, name='nome')
]