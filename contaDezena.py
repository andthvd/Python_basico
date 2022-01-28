def main():
    num = int(input("Digite um número inteiro: "))
    cont = 0
    while cont<1:
        num = num//10
        cont = cont+1
    num = num%10
    print("O dígito das dezenas é",num)           
main()
