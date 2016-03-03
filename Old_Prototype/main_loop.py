import acoes
import mensagens
import recursos

def ler_teclado():
    ler = raw_input()
    return ler


def lista_possibilidades():
    acoes = "Matar Orcs"
    return acoes


def sair_jogo():
    return True



def main_loop():
    exit_game = False

    stamina = recursos.recurso_inicial()

    mensagens.bem_vindo()

    while exit_game != True:

        mensagens.mostra_recursos(stamina)

        escolha = ler_teclado()

        if(escolha == "opcoes"):
            lista_acoes = lista_possibilidades()
            print "Tens as seguintes acoes para fazer: " + lista_acoes

        elif(escolha == "matar orcs"):
            stamina = acoes.cacaorcs(stamina)

        #Sair do jogo digitar SAIR
        if(escolha == "SAIR"):
            exit_game = sair_jogo()


main_loop()




