from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):  # Sempre usa request para uma requisição
    return HttpResponse("Este é Meu Primeiro Site:  Olá")
