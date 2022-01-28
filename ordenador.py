import random
import time


class Ordenador:
    def cria_lista(self, n):
        lista = [random.randrange(100) for x in range(n)]
        return lista

    def lista_quase_ordenada(self, n):
        lista = [x for x in range(n)]
        lista[randon.range(n)] = -500
        return lista
    
    def selecao_direta(self, lista):
        fim = len(lista)

        for i in range(fim -1):
            minimo = i

            for j in range(i+1, fim):
                if lista[j] < lista[minimo]:
                    minimo = j

            lista[i], lista[minimo] = lista[minimo], lista[i]
        return lista

    def bubble_sort(self, lista):
        fim = len(lista)

        for i in range(fim-1, 0, -1):
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
        return lista
    
    def bubble_short(self, lista):
        fim = len(lista)
        for i in range(fim-1, 0, -1):
            trocou = False
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
                    trocou = True
            if not trocou:
                return
        return lista

  

"""if __name__=="__main__":
    
    lista = cria_lista(15)
    print(lista)
    antes = time.time()
    print(selecao_direta(lista))
    depois = time.time()
    print("Algoritmo de seleção direta levou", depois - antes)
    lista = cria_lista(15)
    print(lista)
    antes = time.time()
    print(bubble_sort(lista))
    depois = time.time()
    print("Algoritmo bubblesort levou", depois - antes)
    
"""
