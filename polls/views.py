from django.shortcuts import render

from django.http import HttpResponse
# Trouver un moyen de récuperer tous les livres et de mettre à jour notre base de données avec des hooks

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")