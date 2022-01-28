import ordenador
import random
import time

class ContaTempos:
    def cria_lista(self, n):
        lista = [random.randrange(100) for x in range(n)]
        return lista

    def lista_quase_ordenada(self, n):
        lista = [x for x in range(n)]
        lista[random.randrange(n)] = -500
        return lista

    def compara(self, n):
        lista1 = self.cria_lista(n)
        lista2 = lista1[:]
        
        o = ordenador.Ordenador()

        antes = time.time()
        o.bubble_sort(lista1)
        depois = time.time()
        print("Bolha demorou", depois - antes)

        lista1 = self.lista_quase_ordenada(n)
        lista2 = lista1[:]

        antes = time.time()
        o.bubble_short(lista1)
        depois = time.time()
        print("Bolha curta demorou", depois - antes)
        
