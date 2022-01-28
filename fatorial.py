def fat(n):
    if (n==0) or (n==1):
        return 1
    else:
        return (n*fat(n-1))
def main():
    nu = int(input("Digite um numero a ser calculado a fatorial: "))
    print("A fatorial de",nu,"é igual a",fat(nu))
main()
