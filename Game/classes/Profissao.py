from django.db import models


class Profissao(models.Model):

    tipo = {"Ferreiro", "Alquimista", "Coureiro"}
    
    profissao = models.CharField(PrimaryKey = True ,choices=tipo)
    
    lvl=models.IntegerField
    
    
    