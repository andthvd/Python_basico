def menor_nome(nomes):
    """recebe uma lista de nomes e retorna o nome mais curto"""
    tam = []
    for i in range (len(nomes)):
        nomes[i] = nomes[i].strip().capitalize()
        tam.append(len(nomes[i]))
    nome = ''
    for i in range(len(tam)):
        if tam[i] == min(tam):
            nome = nomes[i]
            break
    return nome


def conta_letras(frase,contar="vogais"):
    assert contar == 'vogais' or contar == 'consoantes'
    frase = frase.lower()
    if contar == 'vogais':
        cont = ['a','e','i','o','u']
    if contar == 'consoantes':
        cont = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    tam = 0
    for i in cont:
        tam += frase.count(i)
    return tam




    
        
