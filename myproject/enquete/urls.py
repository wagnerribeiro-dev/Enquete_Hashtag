from django.urls import path

from . import views  # quando coloca o . pede para trazer todos os arquivos

urlpatterns = [
    path('', views.index, name='index')  # sria padrões de Url
]