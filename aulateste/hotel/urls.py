from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('quartos', views.quartos, name='quartos'),
    path('solteiro', views.quartos_solteiro, name='solteiro'),
    path('casal', views.quartos_casal, name='casal'),
    path('comfort', views.quartos_comfort, name='comfort'),
    path('luxo', views.quartos_luxo, name='luxo'),
    path('cadastro', views.cadastro_user, name='cadastrar'),
    path('login', views.login_user, name='login'),
    path('reserva', views.reservar, name='reserva')
]