from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the site index.")


def lehrer(request): 
    return HttpResponse("Bester Lehrer: Herr Peschel")