from django.db import models

class Classe(models.Model):
  
    tipo = {"Guerreiro", "Mago", "Arqueiro"}
    
    classe = models.CharField(PrimaryKey = True ,choices=tipo)

    # Atributos
    destreza = models.IntegerField
    forca = models.IntegerField
    inteligencia = models.IntegerField
    agilidade = models.IntegerField
    sorte  = models.IntegerField
    vitalidade = models.IntegerField
    
        