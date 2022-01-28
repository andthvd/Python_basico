def dimensao(matriz):
    lin = len(matriz)
    col = len(matriz[0])
    dim = [lin,col]
    return dim
    

def soma_matrizes(m1,m2):
    """ recebe 2 matrizes e devolve uma matriz que represente sua soma caso as matrizes tenham dimensões iguais"""
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

def sao_multiplicaveis(m1,m2):
    """ recebe duas matrizes como parâmetro e devolve True se as matrizes forem multiplicavéis (na ordem dada) e False caso contrário"""
    dim1 = dimensao(m1)
    dim2 = dimensao(m2)
    if dim1[1] == dim2[0]:
        return True
    else:
        return False
