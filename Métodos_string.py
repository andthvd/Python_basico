"""métodos de string

strip()
"slice"[b:e]
count("str")
center(width)
capitalize()
len()
replace()
upper()
lower()
find()
entre outros


"""

def juntastring(string):
    """recebe uma string, elimina os espaços e
    imprime o resultado com a primeira letra maiuscula"""
    pos = 0
    string1 = ""
    while pos < len(string):
        if string[pos] != " ":
            string1 = string1 + string[pos]
        pos = pos + 1
    string1 = string1.capitalize()
    return string1



def lexico(nomes):
    """recebe uma string e returna a menor
string na ordem lexicografica"""
    aux = nomes[0]
    for i in range (len(nomes)):
        if nomes[i].lower() < nomes[i-1].lower():
            aux = nomes[i]
            nomes[i] = nomes[-i]
            nomes[-i] = aux
            
    return nomes


def recebe_nomes():
    """forma uma lista de nomes a partir do que for
digitado pelo usuário"""
    
    nomes = []
    nome = input("Digite um nome (pressione Enter para sair): ")
    while nome:
        nomes.append(nome)
        nome = input("Digite um nome (pressione Enter para sair): ")
    return nomes

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



def reorganiza(nomes):
    """recebe uma lista de nomes e remove os espaços
do inicio e final de frase, retorna a lista com os nomes todos
começando com letra maiuscula"""
    for i in range (len(nomes)):
        nomes[i] = nomes[i].replace(
            nomes[i],
            nomes[i].strip().capitalize()
            )
    return nomes

def testa_menor_string():
    print(teste_pontual(['Andre','      cassio  ', '       luiz'],'Andre'))
    print(teste_pontual(['ana','maria', 'José'],'ana'))
    
    

def teste_pontual(string, resp):
    if (lexico(string)[0]) == resp:
        return "OK!"
    else:
        return "NOK!"

if __name__ == '__main__':
    nomes = ['Andre','      cassio  ', '       luiz']
    nomes = reorganiza(nomes)
    nome = menor_nome(nomes)

                     
