class Race(models.model):

    tipo = {"Humano", "Elfo", "Anao"}

    raca = model.CharField(PrimaryKey = True ,choices=tipo)

    # Atributos
    destreza = models.IntField()
    forca = models.IntField()
    inteligencia = models.IntField()
    agilidade = models.IntField()
    sorte  = models.IntField()
    vitalidade = models.IntField()

    # To-do inicializacao da tabela raca (atributos)