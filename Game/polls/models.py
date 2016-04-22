from django.db import models

class Race(models.Model):

    tipo = (('H','Humano'), ('E','Elfo'), ('A','Anao'))

    race = models.CharField(primary_key=True,choices=tipo,max_length=1)
    
    # Atributos
    destreza = models.IntegerField
    forca = models.IntegerField
    inteligencia = models.IntegerField
    agilidade = models.IntegerField
    sorte  = models.IntegerField
    vitalidade = models.IntegerField


class Profissao(models.Model):

    tipo = (('F','Ferreiro'), ('A','Alquimista'), ('C','Coureiro'))
    
    profissao = models.CharField(primary_key=True,choices=tipo,max_length=1)
    
    lvl=models.IntegerField
    
    
      


class Equipamento(object):
    
    nome=models.CharField(primary_key=True)
    peso=models.IntegerField
    valor=models.IntegerField
    
    
    #modificadores dos stats
    destreza = models.IntegerField
    forca = models.IntegerField
    inteligencia = models.IntegerField
    agilidade = models.IntegerField
    sorte  = models.IntegerField
    vitalidade = models.IntegerField
    
        
class Inventorio(models.Model):
    
    
    id=models.IntegerField(primary_key=True)
    #equipamento=models.ManyToOneRel(Equipamento)
    
    
class Classe(models.Model):
  
    tipo = (('G','Guerreiro'), ('M','Mago'), ('A','Arqueiro'))
    
    classe = models.CharField(primary_key=True,choices=tipo,max_length=1)

    # Atributos
    destreza = models.IntegerField
    forca = models.IntegerField
    inteligencia = models.IntegerField
    agilidade = models.IntegerField
    sorte  = models.IntegerField
    vitalidade = models.IntegerField
    
        
    
class Personagem(models.Model):
    user_name = models.CharField(primary_key = True,max_length=64)


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
    

    
  