def soma_elementos(x):
    soma = 0
    for i in x:
        soma = soma+i
    return soma

def main():
    lista = [1,2,3,4,5,6,7]
    print(soma_elementos(lista))
    #ou
    #print(sum(lista))    
main()
