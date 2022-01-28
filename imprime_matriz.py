def imprime_matriz(m):
    "recebe uma matriz como parâmetro e imprime a matriz, linha por linha"
    lin = len(m)
    col = len(m[0])
    for i in range(lin):
        for j in range (col):
            if j != (col-1):
                print (m[i][j],end=' ')
            else:
                print (m[i][j],end='')
        print()
    return None

def dimensao(matriz):
    lin = len(matriz)
    col = len(matriz[0])
    dim = [lin,col]
    return dim
    

def soma_matrizes(m1,m2):
    soma = []
    dim = []
    if dimensao(m1) == dimensao(m2):
        dim = dimensao(m1)
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

def multiplicaveis(m1,m2):
    dim1 = dimensao(m1)
    dim2 = dimensao(m2)
    if dim1[1] == dim2[0]:
        return True
    else:
        return False

def criar_matriz(linhas,colunas):
    matriz = []
    for i in range (0,linhas):
        linha = []
        for j in range (0,colunas):
            linha.append(input("Digite o elemento correspondente a linha "
                               "{} e coluna {}: ".format(i+1,j+1)))
        matriz.append(linha)
    return matriz
