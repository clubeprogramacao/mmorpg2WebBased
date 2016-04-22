from django.db import models


class Race(models.Model):

    tipo = {"Humano", "Elfo", "Anao"}

    race = models.CharField(PrimaryKey = True ,choices=tipo)

    # Atributos
    destreza = models.IntegerField
    forca = models.IntegerField
    inteligencia = models.IntegerField
    agilidade = models.IntegerField
    sorte  = models.IntegerField
    vitalidade = models.IntegerField

    # To-do inicializacao da tabela raca (atributos)