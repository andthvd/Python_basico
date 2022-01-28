import time
import busca
import random

class ContaTempos:
    def lista_aleatoria(self, n):
        lista = [random.randrange(1000) for x in range(n)]
        return lista

    def lista_quase_ordenada(self, n):
        lista = [x for x in range(n)]
        lista[ random.randrange(n//3)] = -500
        return lista

    def compara(self, n):
        lista1 = self.lista_aleatoria(n)
        lista2 = lista1[:]
        lista3 = self.lista_quase_ordenada(500)

        o = busca.Ordenador()

        antes = time.time()
        o.bolha(lista1)
        depois = time.time()
        print("Bolha demorou {} segundos.".format(depois - antes))
        
        antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print("Seleção direta demorou {} segundos.".format(depois - antes))


        antes = time.time()
        o.bolha_plus(lista3)
        depois = time.time()
        print("Bolha plus demorou {} segundos.".format(depois - antes))
        
        
    
if __name__ == '__main__':
    c = ContaTempos()
    c.compara(1000)
