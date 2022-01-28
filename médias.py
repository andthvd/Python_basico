def calculaMH(conjunto):
    #calcula média armonica
    numerador = len(conjunto)
    lista = []
    if numerador == 2:
        num = (2 *  conjunto[0] * conjunto[1])
        den = conjunto[0] + conjunto[1]
        return (num / den)
    else:
        for i in conjunto:
            lista.append(1 / i)
        return round((numerador / sum(lista)),2)

def calculaMA(conjunto):
    #calcula média aritimetica
    return round((sum(conjunto)/len(conjunto)),2)


#def calculaMP(conjunto):

def calculaMG(conjunto):
    #calcula média geométrica
    numerador = len(conjunto)
    mediaG = 1
    for i in conjunto:
        mediaG *= i
    return round((mediaG ** (1/numerador)),2)
    

def conjunto():
    #retorna um conjunto com os números digitados
    conjunto = []
    elemento = 1
    while elemento != 0:
        i = 1
        elemento = int(input("""(Digite zero para sair)\n
Digite o {} elemento: """.format(i)))
        conjunto.append(elemento)
        i+=1
    if conjunto[-1] == 0:
        del conjunto[-1]
    return conjunto

if __name__ == '__main__':
    conjunto = conjunto()
    print("Média Aritimética é igual a {}".format(calculaMA(conjunto)))
    print("Média Geométrica é igual a {}".format(calculaMG(conjunto)))
    print("Média Harmônica é igual a {}".format(calculaMH(conjunto)))
    
