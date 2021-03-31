from django.http import HttpResponse
# from django.shortcuts import render


def home(request):
    return HttpResponse('Py392: Projeto Django: Depoly automático no Heroku')
