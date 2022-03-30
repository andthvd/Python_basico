import re

def Valida_cpf(cpf):
    #realiza um calculo com o CPF
    print('''Só um minuto que estamos validando a informação''')
    cpf = Converte_cpf(cpf)
    soma = 0
    cpf2 = cpf[0:9]
    print('Validando primeiro digito')
    for p,r in enumerate(range(10,1,-1)):
        soma += int(cpf2[p]) * r
    digito_1 = Digito(soma)
    cpf2 = cpf2 + digito_1
    soma = 0
    print(f'Digito 1: {digito_1}')
    print('Validando segundo digito')
    for p, r in enumerate(range(11,1,-1)):
        soma += int(cpf2[p]) * r
    digito_2 = Digito(soma)
    cpf2 = cpf2 + digito_2
    print(f'Digito 2: {digito_2}')
    if cpf == cpf2:
        return 'CPF VERDADERO'
    else:
        return 'CPF FALSO'
    
        
def Digito(soma):
    resultado = (11-(soma %11))
    if resultado > 9:
        digito_1 = 0
    else:
        digito_1 = resultado
    return str(resultado)


def Converte_cpf(cpf):
    cpf_int = []
    for i in cpf:
        if i.isdigit():
            cpf_int.append(i)
    cpf_int = ''.join(cpf_int)
    return cpf_int


if __name__ == '__main__':
    regex = re.compile('\d{3}.\d{3}.\d{3}-\d{2}$')
    cpf = input('Insira um número de CPF: ')   
    while not regex.findall(cpf):
        cpf = input('Insira um CPF válido!!\n:')
    print(Valida_cpf(cpf))
    
    
    
    
    
