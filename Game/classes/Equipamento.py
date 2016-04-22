from django.db import models


class Equipamento(object):
    
    nome=models.CharField(PrimaryKey=True)
    peso=models.IntegerField
    valor=models.IntegerField
    
    
    #modificadores dos stats
    destreza = models.IntegerField
    forca = models.IntegerField
    inteligencia = models.IntegerField
    agilidade = models.IntegerField
    sorte  = models.IntegerField
    vitalidade = models.IntegerField
    
        
    
    

