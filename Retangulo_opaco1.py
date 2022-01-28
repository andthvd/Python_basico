larg = int(input("digite a largura: "))
alt = int(input("digite a altura: "))
aux = larg
while alt !=0:
    while larg !=0:
        print("#",end='')
        larg = larg-1
    alt = alt-1
    larg = aux
    print()
