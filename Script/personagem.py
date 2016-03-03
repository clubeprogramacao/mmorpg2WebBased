from django.db import models

class Personagem(models.model):
    user_name = models.CharField(primary_key = True)


    # Geral
    hitpoints = models.FloatField()
    max_weight = models.FloatField()
    stamina = models.IntField()
    energia = models.IntField()
    gold = models.IntField()

    # Atributos
    destreza = models.IntField()
    forca = models.IntField()
    inteligencia = models.IntField()
    agilidade = models.IntField()
    sorte  = models.IntField()
    vitalidade = models.IntField()

    # Modulos
    raca = models.ForeignKey(Race) #Done
    craft = models.ForeignKey(Craft)
    profissao = models.ForeignKey(Profissao)
    classe = models.ForeignKey(Classe)
    inventory = models.ManyToMany(Inventorio)


