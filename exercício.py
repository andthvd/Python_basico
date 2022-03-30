def soma_lista(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + soma_lista(lista[1:])  
    

def encontra_impares(l, i=0, lista_impares=[]):
    try:
        e = l[i] if l[i]%2!=0 else None
        i+=1
        if e:
            lista_impares.append(e)
        return encontra_impares(l,i,lista_impares) 
    except:
        return lista_impares



def incomodam(n):
    if n <= 0:
        return print(str())
    if n == 1:
        return "incomodam "
    else:        
        return "incomodam " + incomodam(n-1)

def elefantes(n, i=1):
    if n <= 1:
        return str("")
    for i in range(i, n+1):
        if n <= 1:
            return str()
        if i == 1:
            return "Um elefante incomoda muita gente\n" + "{} elefantes ".format(str(i+1)) + str(incomodam(i+1)) + "muito mais\n" + str(elefantes(n, i+2)) 
        else:
            return "{} elefantes incomodam muita gente\n".format(str(i-1)) + "{} elefantes ".format(str(i)) + str(incomodam(i)) + "muito mais\n" + str(elefantes(n, i+1))
    return str("")




def contador():

    for p,r in enumerate(range(10,1,-1)):
        print(p, r)
 
