import string
import re

def maiusculas(frase):
    lista = ""
    
    for i in frase:
        if ord(i) in range(65,91):
            lista += i
    return lista

if __name__ == '__main__':
    frase = 'PrOgRaMaMoS em python!'
    maiusculas(frase)
            
