def calculaPrimo(x):
    fat = 2
    while x % fat != 0 and fat <= ( x / 2 ):
        fat += 1
    if x == 2:
        return True
    if x % fat == 0:
        return False
    else:
        return True

def listaPrimo(x):
    lista = []
    for n in range (2, x + 1):
        if calculaPrimo(n):
            lista.append(n)
            pass
    return lista

def ePrimo(x):
    if x in listaPrimo(x):
        return True
    else:
        return False
    


