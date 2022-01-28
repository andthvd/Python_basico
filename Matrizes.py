
def imprime_mat(x):
    for i in x:
        for j in range(5):
            print(i,end='')
        print()
    

def crie_mat(n_l, n_c, valor):
    '''(int, int, valor) -> matriz (lista de listas)
    Cria e returna uma matriz com n_l linhas
    e n_c colunas em que cada elemento é igual
    ao valor dado. '''

    matriz = [] #lista vazia
    for i in range(n_l):
        linha = []

        for j in range(n_c):

            linha.append(valor)

        matriz.append(linha)
    return matriz

def main():
    A = crie_mat(5,5,0)
    imprime_mat(A)
main()


        
            
