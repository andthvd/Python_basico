larg = int(input("digite a largura: "))
alt = int(input("digite a altura: "))
aux = larg
aux2 = alt
while alt !=0:
    if alt == aux2 or alt == 1:
        while larg !=0:
            print("#",end='')
            larg = larg-1
    else:
        while larg !=0:
            if larg == aux or larg ==1:
                print("#",end='')
                pass
            else: print(" ",end='')
            larg = larg-1
    alt = alt-1
    larg = aux
    print()
