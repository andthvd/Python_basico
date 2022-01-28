n_glob = int(1)
m_glob = int(1)
placar_u = int(0)
placar_c = int(0)
jogada = int(1)
alter = True

def computador_escolhe_jogada(n_com,m_com):
    global n_glob
    global jogada
    jogada = m_com
    while jogada != 0:
        if ((n_com-jogada)%(m_com+1)==0) and (jogada > 1):
            print()
            print("Computador tirou",jogada," peças.")
            n_glob=n_com-jogada
            return print("Agora restam",n_glob,"no tabuleiro.")
        elif ((n_com-jogada)%(m_com+1)==0) and (jogada == 1):
            print()
            print("Computador tirou uma peça.")
            n_glob=n_com-jogada
            return print("Agora restam",n_glob,"no tabuleiro.")
        elif (jogada == 1):
            print()
            print("Computador tirou uma peça.")
            n_glob=n_com-jogada
            return print("Agora restam",n_glob,"no tabuleiro.")
        else:
            jogada = jogada-1
            pass
    
def usuario_escolhe_jogada(n_usu,m_usu):
    global n_glob
    global jogada
    print()
    jogada = int(input("Quantas peças você vai tirar? "))
    while ((jogada <= m_usu)and(jogada > 0)):
        if (jogada == 1):
            print("Você tirou uma peça.")
            n_glob = n_usu-jogada
            return print("Agora restam",n_glob,"no tabuleiro.")
        else:
            print("Você tirou",jogada,"peças")
            n_glob = n_usu-jogada
            return print("Agora restam",n_glob,"no tabuleiro.")
    print()
    print("Oops! Jogada inválida! Tente de novo.")
    usuario_escolhe_jogada(n_usu,m_usu)

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
    if (n_glob==2):
        if m_glob in (2,3):
            n_glob=0
            pass
    if (n_glob==1 and m_glob==1):
        print()
        n_glob=0
        pass
    if ((m_glob)<(n_glob)) and (n_glob != 0):
        if ((n_glob)%(m_glob+1)==0):
            print()
            print("Você começa!")
            usuario_escolhe_jogada(n_glob,m_glob)
            alter = False
            pass
        else:
            print()
            print("Computador começa!")
            computador_escolhe_jogada(n_glob,m_glob)
            alter = True
            pass
    while n_glob != 0:
        if (alter == False):
            computador_escolhe_jogada(n_glob,m_glob)
            alter = True
            pass
        elif (alter == True):
            usuario_escolhe_jogada(n_glob,m_glob)            
            alter = False
            pass
    if (alter == True):
        print()
        print("Fim do jogo! O computador venceu!")
        placar_c = placar_c + 1
        pass
    else:
        print()
        print("Fim do jogo! Você venceu!")
        placar_u = placar_u + 1
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
