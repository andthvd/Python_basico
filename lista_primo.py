listaPrimo = []

def calculaPrimo(x):
    fat =2
    while x%fat !=0 and fat<=(x/2):
        fat=fat+1
    if x==2:
        return True

    if x%fat ==0:
        return False
    else:
        return True

def main():
    global listaPrimo
    for n in range (2,1000):
        if calculaPrimo(n):
            listaPrimo.append(n)
        else:
            print(n, "não é primo!")
main()
