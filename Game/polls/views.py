from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Race
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
    raca=Race(raca='H',destreza=20,forca=10,inteligencia=15,agilidade=29,sorte=0,vitalidade=100)
    raca.save()