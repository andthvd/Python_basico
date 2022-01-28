"""Algoritmos de busca"""


def busca(lista, termo):
    #Busca Sequencial
    #BOA, MAS EM UMA LISTA MUITO GRANDE EXIGE GRANDE PROCESSAMENTO
    """(list, float) -> bool"""
    for i in range(len(lista)):
        if lista[i] == termo:
            return i
    return False

class Musica:
    def __init__(self, titulo, interprete, compositor, ano):
        self.titulo = titulo
        self.interprete = interprete
        self.compositor = compositor
        self.ano = ano

class Buscador:
    def busca_por_titulo(self, seq, x):
        for i in range(len(seq)):
            if seq[i].titulo == x:
                return i
        return -1

    def vamos_buscar(self):
        playlist = [ Musica("Ponta de Areia", "Milton Nascimento", "Milton Nascimento", 1975),
                     Musica("Podres Poderes", "Caetano Veloso", "Caetano Veloso", 1984),
                     Musica("Baby", "Gal Costa", "Caetano Veloso", 1969)]
        onde_achou = self.busca_por_titulo(playlist, "Baby")

        if onde_achou == -1:
            print("Minha música preferida não está na playlist")
        else:
            preferida = playlist[onde_achou]
            print(preferida.titulo, preferida.interprete, preferida.compositor, preferida.ano,
                  sep = ', ');
            
            
"""Algoritmos de Ordenação"""

#Seleção Direta

class Ordenador:
    def selecao_direta(self, lista):
        fim = len(lista)

        for i in range(fim - 1):
            #Inicialmente, o menor elemento já visto é o i-ésimo
            posicao_do_minimo = i

            for j in range(i+1, fim):
                if lista[j] < lista[posicao_do_minimo]:
                    posicao_do_minimo = j

            #Coloca o menor elemento encontrado no início da sub-lista
            #Para isso, troca de lugar os elementos das posições i e posicao_do_minimo
            lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]


import random

def lista_grande(n):
    lista = []
    for i in range(n):
        lista.append(random.randint(0, n))
    return lista


def ordenada(lista):
    b = Ordenador()
    x = lista[:]
    b.selecao_direta(x)
    if lista == x:
        return True
    else:
        return False
                 
def ordena(lista):
    b = Ordenador()
    b.selecao_direta(lista)
    return lista


def retira_duplicado(seq):
    seq2 = []
    fim = len(seq)
    for i in seq:
        if (seq.count(i)) > 1:
            del seq[busca(seq, i)]
    return seq

def organiza(seq):
    fim = len(seq)
    for i in range(fim - 1):
        minimo = i
        for j in range(i+1, fim):
            if seq[j] < seq[minimo]:
                minimo = j
        seq[i], seq[minimo] = seq[minimo], seq[i]
    
    
"""Algoritmo de Busca Binária
 a cada iteração metade da sequência é eliminada da busca.
 Dessa forma, usando o algoritmo de busca sequencial
 em uma sequência com 1024 elementos, todos os 1024 elementos
 devem ser testados antes do algoritmo
 indicar que o elemento não está na lista. No caso da busca binária,
 o primeiro teste elimina 512 elementos, o segundo 256, o terceiro 128,
 e depois 64, 32, 16, 8, 4, 2, até que a lista contenha apenas 1 elemento.
 Dessa forma, ao invés de 1024, apenas 10 elementos
 (ou log(len(seq))) precisam ser testados."""




def buscaBinaria(seq, x):
    primeiro = 0
    ultimo = len(seq)-1
    ordena(seq)

    while primeiro <= ultimo:
        meio = (primeiro + ultimo)//2
        if seq[meio] == x:
            return meio
        else:
            if x < seq[meio]:
                ultimo = meio - 1
            else:
                primeiro = meio + 1
    return False

seq = [20,12,32,11,20,31,64,20,11,82,65,10]
print(buscaBinaria(seq, 20))

        
