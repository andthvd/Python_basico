def primeiro_lex(nomes):
    """recebe uma string e returna a menor
string na ordem lexicografica utilizando o método bolha"""
    fim = len(nomes)
    for x in range (fim-1,0,-1):
        for i in range (x):
            if nomes[i].lower() > nomes[i+1].lower():
                nomes[i], nomes[i+1] = nomes[i+1], nomes[i]            
    return nomes[0]
