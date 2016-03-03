# Este script e para determinar as diversas acoes possiveis do jogo
#
# Criador: Victor Carvalho
# Data criacao: 17/02/2016
# Ultima modificacao: 17/02/2016
#
# Este modulo define as classes que serao usadas para se IDENTIFICAR acoes dentro do jogo
# Devolve valores True ou False para cada tipo de missao, por exemplo, mudou de cidade ou foi matar orcs

import recursos

def cacaorcs(recursoAtual):
    print "Foi matar orcs"
    return recursos.diminuiRecurso(recursoAtual)



