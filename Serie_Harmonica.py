def serieHarmonica(n):
    serie_Harmonica = []
    numerador = 1
    denominador = 1
    for i in range(n):
        serie_Harmonica.append(
            numerador / denominador
            )
        denominador += 1
    return serie_Harmonica

def serieHarmonica_invertida(n):
    serie_Harmonica_invertida = []
    numerador = 1
    denominador = n
    for i in range(n):
        serie_Harmonica_invertida.append(
            numerador / denominador
            )
        denominador -= 1
    return serie_Harmonica_invertida

def imprime(n):
    for i in range(0,len(n),3):
        print("{}\t{}\t{}".format(n[i],n[i+1],n[i+2]))
    
def serieComparativa(n):
    serie_Harmonica = [1]
    numerador = 1    
    for i in range(n-1):
        k = 2**i
        serie_Harmonica.append(
            (k / 2)
            *(numerador / k)
            )
    return serie_Harmonica

def serieComparativa2(n):
    serie_Harmonica = [1]
    for i in range(n-1):
        serie_Harmonica.append(
            1/2
            )
    return serie_Harmonica
    
if __name__ == '__main__':
    sh = serieComparativa(10)
    sh2 = serieComparativa2(10)

