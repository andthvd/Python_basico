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


def ordena(lista):
    b = Ordenador()
    b.selecao_direta(lista)
    return lista

def busca(seq, x):
    primeiro = 0
    ultimo = len(seq) - 1
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
    return -1

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


    def bolha(self, lista):
        fim = len(lista)

        for i in range(fim - 1, 0, -1):
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]

    def bolha_plus(self, lista):
        fim = len(lista)
        
        for i in range(fim - 1, 0, -1):
            trocou = False
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
                    trocou = True
            if not trocou:
                return


def bubble_sort(lista):
    b = Ordenador()
    b.bolha_plus(lista)
    return lista
    
    
