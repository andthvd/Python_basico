nome ="C:/Users/andre.santos/Documents/dev/poesia.txt"

with open(nome, 'w+', encoding='utf-8')as arq:
    arq.write("     O poeta é um fingidor.      \n")
    arq.write("     Finge tão completamente     \n")
    arq.write("     Que chega a fingir que é dor\n")
    arq.write("     A dor que deveras sente.    \n")
    arq.write("                 Fernando Pessoa.\n")
    conteudo = arq.read()


with open(nome, 'r', encoding='utf-8')as arq:
    for linha in arq:
        print(linha.strip())
    conteudo = arq.read()
