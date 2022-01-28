import os


def calcula_nota(lista):
    """Calcula a media de acertos pelo numero de questões"""
    media = sum(lista)/len(lista)
    return (media * 100)

def produto_nota(acertos, peso_questao):
    """Calcula os acertos x o peso por questão, e retorna a nota"""
    assert len(acertos) == len(peso_questao)
    n = len(acertos)
    lista = []
    for i in range(n):
        lista.append(
            acertos[i] * peso_questao[i]
            )
    return sum(lista)
    

def le_acerto():
    """Retorna uma lista de acertos com valores digitados pelo usuario"""
    n = (int(input("Digite o número de questões na prova: ")))
    lista_notas = []
    for i in range(n):
        os.system('cls')
        lista_notas.append(int(input("Questão {}):\nDigite 1 para acerto"
                       " e 0 para erro: ".format(i+1)
                                     )))
    return lista_notas

def le_peso_notas():
    """Retorna uma lista com o peso/questão"""
    n = (int(input("Digite o número de questões na prova: ")))
    peso_quest = []
    flag = 0
    while flag == 0:
        peso_quest.clear
        flag = 1
        for i in range(n):
            os.system('cls')
            peso_quest.append(float(input("Questão {}):\n"
                               "Digite o peso da questão: ".format(i+1)
                               )))
        if sum(peso_quest) == 10:
            return peso_quest
        else:
            print("A soma do peso das questões precisa ser igual a 100!!")
            flag = 0



def menu():
    flag = 0
    peso = []
    notas = []
    acertos = []
    while flag == 0:
        botao = int(input("""Bem vindo ao calculador de notas

1: Inserir peso por questão
2: Verificar acerto por questão
3: Calcular nota

_"""))
        if botao == 1:
            peso = le_peso_notas()
            pass
        elif botao == 2:
            acertos = le_acerto()
            pass
        elif botao == 3:
            assert acertos
            if peso:
                notas = produto_nota(acertos, peso)
                print("A sua nota final é: {}".format(notas))
                os.system("cls")
                flag = int(input("""Deseja calcular a nota de outro teste?

0: Sim
1: Não

_"""))
                pass
            else:
                notas = calcula_nota(acertos)
                print("A sua nota final é: {}".format(notas))
                os.system("cls")
                flag = int(input("""Deseja calcular a nota de outro teste?

0: Sim
1: Não

_"""))
                pass
                
            

if __name__ == "__main__":
    menu()               
