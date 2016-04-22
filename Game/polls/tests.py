from django.test import TestCase
from polls.models import Race

# Create your tests here.


raca=Race(raca='H',destreza=20,forca=10,inteligencia=15,agilidade=29,sorte=0,vitalidade=100)
raca.save()