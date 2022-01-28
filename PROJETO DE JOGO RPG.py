import random


class Char:

    def __init__(self, atributos):
        self.nome   = atributos[0]
        self.atq    = atributos[1]
        self.dfs    = atributos[2]
        self.pv     = atributos[3]

    def ataque(self, c2):
        dano = (self.atq - c2.dfs)        
        c2.pv -= (dano
                  + random.randint(1,3))
        return print("{} causou {} de dano em {}".format(self.nome, dano, c2.nome))

def cria_personagem():
    nome = input("Digite o nome do personagem: ")
    atributos = [nome]
    for i in range(3):
        atributos.append(random.randint(4,12))
    return atributos


def luta(a,b):
    fim = [a,b]
    while 0 not in fim:
        for i in range(10):
            if (i%2)==0:
                a.ataque(b)
            else:
                b.ataque(a)
        print("{} está com {} de vida, e {} está com {} de vida".format(a.nome, a.pv, b.nome, b.pv))
        break

    
if __name__ == '__main__':
    pers1, pers2 = ['Personagem1', 5, 5, 12], ['Personagem2', 7, 4, 7]
    pers1, pers2 = Char(pers1), Char(pers2)
    luta(pers1, pers2)

