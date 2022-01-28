import os
import time

def calcula_nota(lista):
    """Calcula a media de acertos pelo numero de questões"""
    media = sum(lista)/len(lista)
    return (media * 100)

def recebe_respostas():
    os.system('cls')
    n = 'a'
    i = 0
    lista = []
    while n != '':
        i += 1
        n = input("Digite a resposta da Questão {}: ".format(i))
        lista.append(n)
    if lista[-1] == '':
        del lista[-1]
    return lista

def compara_respostas(lista1, lista2):
    assert len(lista1) == len(lista2)
    acertos = []
    for i in range(len(lista1)):
        if lista1[i] == lista2[i]:
            acertos.append(1)
        else:
            acertos.append(0)
    return acertos

if __name__ == '__main__':
    print("Digite as SUAS respostas...(TECLE ENTER PRA SAIR)")
    time.sleep(3)
    aluno_respostas = recebe_respostas()
    os.system('cls')
    print("Digite o gabarito...(TECLE ENTER PRA SAIR)")
    time.sleep(1)
    gabarito_respostas = recebe_respostas()
    os.system('cls')
    print("Agora vamos comparar suas respostas com o gabarito...")
    time.sleep(1)
    acertos = compara_respostas(aluno_respostas, gabarito_respostas)
    nota = round(calcula_nota(acertos),2)
    print("\nSeus acertos: {}\nA sua média foi {}".format(acertos,nota))
    
    
    

    
