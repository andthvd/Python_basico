import os
def main():
    num1 = int(input("Digite a primeira nota:"))
    num2 = int(input("Digite a segunda nota:"))
    num3 = int(input("Digite a terceira nota:"))
    num4 = int(input("Digite a quarta nota:"))
    media = float((num1+num2+num3+num4)/4)
    print("A média aritmética é",media)
    os.system('pause')
main()

