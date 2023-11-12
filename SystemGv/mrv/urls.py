# urls.py

from django.urls import path
from .views import criar_receituario, lista_receituarios
urlpatterns = [
    path('criar-receituario/', criar_receituario, name='criar_receituario'),
    path('lista-receituarios/', lista_receituarios, name='lista_receituarios'),
]
