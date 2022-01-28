

def remove_repetidos(x):
    x = sorted(x)
    lista2 = []
    for i in range (0,(max(x)+1)):
        if i in x:
            lista2.append(i)
    return lista2
    
def main():
    lista = [2,4,2,2,3,3,1] 
main()

    
