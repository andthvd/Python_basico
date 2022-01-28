n_glob = int(1)
m_glob = int(1)
placar_u = int(0)
placar_c = int(0)
jogada = int(1)
alter = True

def computador_escolhe_jogada(n_com,m_com):
    global n_glob
    global jogada
    if (n_com <= m_com):
        return n_com
    else:
        resto = n_com % (m_com+1)
        if resto > 0:
            return resto
        return m_com
    
def usuario_escolhe_jogada(n_usu,m_usu):
    global n_glob
    global jogada
    print()
    jogada = 0
    while jogada == 0:
        jogada = int(input("Quantas peças você vai tirar? "))

        if (jogada > n_usu) or (jogada < 1) or (jogada > m_usu):
            print("\nOops! Jogada inválida! Tente de novo.\n")
            jogada = 0
    return jogada

def campeonato():
    rodada_campeonato = int(1)
    print()
    print("Voce escolheu um campeonato!")
    while (rodada_campeonato <= 3):
        print()
        print("**** Rodada",rodada_campeonato,"****")
        print()
        partida()
        rodada_campeonato = (rodada_campeonato+1)
    print()
    print("**** Final do campeonato! ****")
    print()
    print("Placar: Você",placar_u,"X",placar_c,"Computador")
    return 0
            
def partida():
    global placar_u
    global placar_c
    global jogada
    global n_glob
    global m_glob
    global alter
    n_glob = int(input("Quantas peças? "))
    m_glob = int(input("Limite de peças por jogada? "))
    if (n_glob % (m_glob+1) == 0):
        print("\nVocê começa!")
        alter = False
    else:
        print("\nComputador começa!")
    while n_glob > 0:
        if alter:
            jogada = computador_escolhe_jogada(n_glob,m_glob)
            alter=False
            if jogada ==1:
                print("\nComputador retirou uma peça.")
                pass
            else: print("\nComputador retirou",jogada,"peças.")
        else:
            jogada = usuario_escolhe_jogada(n_glob,m_glob)
            alter=True
            if jogada ==1:
                print("Você retirou uma peça.")
                pass
            else: print("Você retirou",jogada,"peças.")
        n_glob = (n_glob - jogada)
        if n_glob == 1:
            print("Agora resta apenas uma peça no tabuleiro.\n")
            pass
        elif n_glob <=0:
            pass
        else: print("Agora restam apenas",n_glob,"peças no tabuleiro.\n")
        
    if alter:
        print("Fim do jogo! Você venceu!")
        placar_u = placar_u + 1
        pass
    else:
        print("Fim do jogo! O computador venceu!")
        placar_c = placar_c + 1
        pass
        
                  

def main():
    escolha = int(input("""Bem-vindo ao jogo do NIM! Escolha:

1 - para jogar uma partida isolada
2 - para jogar um campeonato """))
    if ((escolha <=2) and (escolha > 0)):
        if (escolha == 1):
            print()
            print("Você escolheu uma partida isolada!")
            print()
            partida()
            pass
        elif (escolha == 2):
            campeonato()
            pass
    else:
        print()
        print("Escolha uma opção valida!!!")
        print()
        main()     
main()
