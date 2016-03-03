# Este script e para os recursos do jogo
#
# Criador: Victor Carvalho
# Data criacao: 17/02/2016
# Ultima modificacao: 17/02/2016
#
# Este modulo define as classes que serao usadas para se realizar acoes dentro do jogo
# Das mais basicas como ir a uma missao(Stamina) como os propios recursos de crafting(?)

def recurso_inicial():
    recursoInicial = 5
    return recursoInicial

#Diminui o numero de recursos atual
def diminuiRecurso(recursoAtual):
    recursoAtual -= 1
    return recursoAtual

