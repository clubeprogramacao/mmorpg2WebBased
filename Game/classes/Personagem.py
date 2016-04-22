from django.db import models
from classes.Race import Race
from classes.Profissao import Profissao
from classes.Classe import Classe
from classes.Inventorio import Inventorio

class Personagem(models.Model):
    user_name = models.CharField(primary_key = True)


    # Geral
    hitpoints = models.FloatField()
    max_weight = models.FloatField()
    stamina = models.IntegerField
    energia = models.IntegerField
    gold = models.IntegerField

    # Atributos
    destreza = models.IntegerField
    forca = models.IntegerField
    inteligencia = models.IntegerField
    agilidade = models.IntegerField
    sorte  = models.IntegerField
    vitalidade = models.IntegerField

    # Modulos
    raca = models.ForeignKey(Race) #Done
   # craft = models.ForeignKey(Craft)
    profissao = models.ForeignKey(Profissao)
    classe = models.ForeignKey(Classe)
    inventory = models.ForeignKey(Inventorio)
    


