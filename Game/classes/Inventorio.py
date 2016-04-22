from django.db import models
from classes.Equipamento import Equipamento


class Inventorio(models.Model):
    
    
    id=models.IntegerField(primary_key = True)
    equipamento=models.ManyToOneRel(Equipamento)
    
    
    
    
    
    
    