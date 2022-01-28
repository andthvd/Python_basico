def imprime_matriz(m):
    "recebe uma matriz como parâmetro e imprime a matriz, linha por linha"
    lin,col = len(m),len(m[0])
    for i in range(lin):
        for j in range (col):
            if j != (col-1):
                print (m[i][j],end=' ')
            else:
                print (m[i][j],end='')
        print()

def dimensoes(matriz):
    "recebe uma matriz como parâmetro e imprime as dimensões da matriz recebida, no formato iXj"
    lin = len(matriz)
    col = len(matriz[0])
    dim = [lin,col]
    return dim
    

def soma_matrizes(m1,m2):
    """ recebe 2 matrizes e devolve uma matriz que represente sua soma caso as matrizes tenham dimensões iguais"""
    soma = []
    dim = []
    if dimensoes(m1) == dimensoes(m2):
        dim = dimensoes(m1)
        lin = dim[0]
        col = dim[1]
        for i in range (lin):
            linha = []
            for j in range (col):
                linha.append(m1[i][j]
                             +m2[i][j])
            soma.append(linha)
        return soma
    else:
        return False

def sao_multiplicaveis(m1,m2):
    """ recebe duas matrizes como parâmetro e devolve True se as matrizes forem multiplicavéis (na ordem dada) e False caso contrário"""
    dim1 = dimensoes(m1)
    dim2 = dimensoes(m2)
    if dim1[1] == dim2[0]:
        return True
    else:
        return False


def criar_matriz(linhas,colunas):
    "Cria uma matriz onde o usuario digita o valor de suas celulas"
    matriz = []
    for i in range (0,linhas):
        linha = []
        for j in range (0,colunas):
            linha.append(input("Digite o elemento correspondente a linha "
                               "{} e coluna {}: ".format(i+1,j+1)))
        matriz.append(linha)
    return matriz

def nul_lines(matriz):
    """ inteiros positivos m e n e os elementos de uma matriz A de números inteiros
de dimensão m x n e conta o número de linhas e colunas que tem apenas zeros."""
    lin = len(matriz)
    col = len(matriz[0])
    nul_lin = 0
    nul_col = 0
    aux = 0
    for i in range (lin):
        aux = 0
        for j in range (col):
            print("{}x{}".format(i,j),matriz[i][j])
            if matriz[i][j] != 0:
                aux += 1
        if aux == 0:
            nul_lin += 1
    for i in range (col):
        aux = 0
        for j in range (lin):
            print("{}x{}".format(j,i),matriz[j][i])
            if matriz[j][i] != 0:
                aux += 1
        if aux == 0:
            nul_col += 1
    print("Linhas nulas = {}".format(nul_lin))
    print("Colunas nulas = {}".format(nul_col))


def criaMatriz(l,c,v):
    """Cria uma matriz de l linhas e c colunas
preenchida inteira com v"""
    matriz = []
    for i in range(l):
        linhas = []
        for j in range(c):
            linhas.append(v)
        matriz.append(linhas)
    return matriz

def criaVetor(x):
    vetor = []
    for i in range (x):
        vetor.append(x)
    return vetor
            

def multiplica_matriz(m1,m2):
    """Recebe duas matrizes e retorna o produto de sua multiplicação,
caso sejam multiplicaveis"""
    if sao_multiplicaveis(m1,m2):
        dim1, dim2 = dimensoes(m1), dimensoes(m2)
        produto = []
        for lin in range(dim1[0]):
            produto.append([])
            for col in range(dim2[1]):
                produto[lin].append(0)
                for k in range(dim1[1]):
                    produto[lin][col] += (
                        m1[lin][k]
                        * m2[k][col]
                        )
        return produto
    else:
        return print("Ops! As matrizes não são multiplicáveis!")
        
if __name__ == '__main__':
    a = [[1, 2, -1], [0, 3, 2]]
    b = [[1, -1], [2, 0], [3, 2]]
    imprime_matriz(multiplica_matriz(a, b))

    
