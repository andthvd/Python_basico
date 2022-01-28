def separa(texto, sep):
    lista = texto.split(sep)
    return lista


def comprimento(lista):
    tam = []
    for i in lista:
        tam.append(len(i))
    return max(tam)
    

def soma(lista):
    num = []
    for i in lista:
        if i.strip().isdigit():
            num.append(int(i))
    return sum(num)


nome = "C:/Users/andre.santos/Documents/dev/exercicio.txt"

with open(nome, mode='w',encoding='utf-8') as arq:
    arq.write("\t5 4 3 2 1\n")
    arq.write("\t4 4 4\n")
    arq.write("\t2.7\n")
    arq.write("\t3.14 2.1\n")
          
conteudo= []
with open(nome, mode='r', encoding='utf-8') as arq:
    for linha in arq:
        conteudo.append(linha)

def separa_lista(lista):
    a = []    
    for i in lista:        
        b = []
        for j in (i.split()):
            a.append(float(j))
            b.append(float(j))
        print(sum(b))
    return sum(a)
