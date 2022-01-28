import re

def le_assinatura():
    #A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos
    print("Bem-vindo ao detector automático de COH-PIAH.")
    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    sAB = 0
    for i in range(0,6):
        aux = as_a[i]
        - as_b[i]
        if aux > 0:
            sAB += (as_a[i] - as_b[i])
        else:
            sAB += (aux
                    * -1)
    return sAB/ 6
        

def calcula_assinatura(texto):
    ass_texto = [
        tamMedioPalavra(texto),relTypeToken(texto),razHapaxLegomana(texto),
        tamMedioSent(texto),CmplxSent (texto),TamMedFrase (texto)
        ]
    return ass_texto
    

def avalia_textos(textos, ass_cp):
       
    grauSAB =[]
    cohpiah = 0
    for i in textos:
        grauSAB.append(
            compara_assinatura(
            calcula_assinatura(i),ass_cp
            ))
        print(calcula_assinatura(i))
    cont = len(grauSAB)
    for i in range(0,cont-1):
        print (grauSAB[i])
        if grauSAB[i] == min(grauSAB):
            copiah = i+1
    return copiah
            
    
    
        

###

def tamMedioPalavra(texto):
    #Calcula o tamanho médio de palavra a partir de um texto
    lista_palavras = extrai_lista(texto)
    tam = 0
    for i in lista_palavras:
        tam += len(i)
    return tam / len(lista_palavras)

def relTypeToken(texto):
    #Calcula a relação Type-Token a partir de um texto
    lista_palavras = extrai_lista(texto)
    pDif = n_palavras_diferentes(lista_palavras)
    return pDif / len(lista_palavras)

def razHapaxLegomana(texto):
    #Calcula a razão Hapax Legomana a partir de um texto
    lista_palavras = extrai_lista(texto)
    pUni = n_palavras_unicas(lista_palavras)
    return pUni / len(lista_palavras)

def tamMedioSent(texto):
    #Calcula o tamanho medio de sentença a partir de um texto
    sentencas = separa_sentencas(texto)
    return calcCharSent(texto) / len(sentencas)

def CmplxSent (texto):
    #Calcula a complexidade das sentenças em um texto
    sentencas = separa_sentencas(texto)
    nFras = 0
    for i in sentencas:
        nFras += len(separa_frases(i))
    return nFras / len(sentencas)

def TamMedFrase (texto):
    #Calcula o numero de caracteres por frase dentro de um texto
    sentencas = separa_sentencas(texto)
    tam = 0
    frases = []
    divisor = 0
    for i in (0,(len(sentencas)-1)):
        frases = (separa_frases(sentencas[i]))
        for p in frases:
            tam += len(p)
            divisor +=1
    
    return tam / divisor
 

def calcChar(texto):
    #calcula o numero de caracteres em um texto, exceto os caracteres ' ,.:;!?.'
    lista_palavras = extrai_lista(texto)
    tam = 0
    for i in lista_palavras:
        tam += len(i)
    return tam

def extrai_lista(texto):
    #extrai uma lista de palavras
    lista_palavras = re.split(r'[ ,.:;!?.]+',texto)
    if lista_palavras[-1] == '':
        del lista_palavras[-1]
    return lista_palavras

def calcCharSent(texto):
    #Calcula o numero de caracteres por sentença dentro de um texto
    sentencas = separa_sentencas(texto)
    tam = 0
    for i in sentencas:
        tam += len(i)
    return tam

def main():    
    """ass_cp = le_assinatura()
    #recebe uma assinatura para comparação

    textos = le_textos()
    
    #forma uma lista de textos a serem comparados com a assinatura"""
    textos = ['Navegadores antigos tinham uma frase gloriosa:"Navegar é preciso; viver não é preciso". Quero para mim o espírito [d]esta frase, transformada a forma para a casar como eu sou: Viver não é necessário; o que é necessário é criar. Não conto gozar a minha vida; nem em gozá-la penso. Só quero torná-la grande,ainda que para isso tenha de ser o meu corpo e a (minha alma) a lenha desse fogo. Só quero torná-la de toda a humanidade;ainda que para isso tenha de a perder como minha. Cada vez mais assim penso.Cada vez mais ponho da essência anímica do meu sangueo propósito impessoal de engrandecer a pátria e contribuirpara a evolução da humanidade.É a forma que em mim tomou o misticismo da nossa Raça.','Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres.','NOSSA alegria diante dum sistema metafisico, nossa satisfação em presença duma construção do pensamento, em que a organização espiritual do mundo se mostra num conjunto lógico, coerente a harmônico, sempre dependem eminentemente da estética; têm a mesma origem que o prazer, que a alta satisfação, sempre serena afinal, que a atividade artística nos proporciona quando cria a ordem e a forma a nos permite abranger com a vista o caos da vida, dando-lhe transparência.']
    ass_cp = [4.79,0.72,0.56,80.5,2.5,31.6]
    

    cohpiah = avalia_textos(textos,ass_cp)

    print ("O autor do texto", cohpiah, "esta infectado com COH-PIAH")
    
main()
