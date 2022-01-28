def criar_matriz(linhas,colunas):
    matriz = []
    for i in range (0,linhas):
        linha = []
        for j in range (0,colunas):
            linha.append(input("Digite o elemento correspondente a linha "
                               "{} e coluna {}: ".format(i+1,j+1)))
        matriz.append(linha)
    return matriz

def main():
    linhas = int(input("Digite o numero de linhas: "))
    colunas = int(input("Digite o numero de colunas: "))
    matriz = (criar_matriz(linhas,colunas))
    for i in matriz:
        print(i,"\n")        
main()
    
