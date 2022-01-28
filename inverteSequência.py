def main():
    n=1
    lista = []
    while n!=0:
        n=int(input("Digite um número: "))
        if n!=0:
            lista.append(n)
    lista2 = lista[::-1]
    for i in lista2:
        print(i)
main()
        
        
