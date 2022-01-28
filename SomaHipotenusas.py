import math
listaHipotenusa=[]

def hipo():
    raizes=[]
    global listaHipotenusa
    a=1
    while a<=100:
        b=1
        while b<=100:
            testeInteiro = int((a*a)+(b*b))
            raizes.append(math.sqrt(testeInteiro))            
            b=b+1
        a=a+1
    for i in range (0,1000):
        if i in raizes:
            listaHipotenusa.append(i)
            pass

def soma_hipotenusas(x):
    soma = 0
    for i in range (0,x+1):
        if i in listaHipotenusa:
            soma = soma+i
            pass
    return soma
    
        


def main():
    hipo()
    global listaHipotenusa
    #n=1
    #while n != 0:
        #n = int(input("Digite um numero: "))
        #print(soma_hipotenusas(n))
    
main()
            
    
