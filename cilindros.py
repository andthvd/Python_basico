import math

class Receita:
    def __init__(self, arroz, alho, oleo, sal):
        self.arroz      = arroz
        self.alho       = alho
        self.oleo       = oleo
        self.sal        = sal

    def razaoIngredientes(self):
        lista = [self.arroz, self.alho,
                 self.oleo, self.sal]
        self.razao = sum(lista) / len(lista)
        

class Cilindro:
    def __init__(self, diametro, raio, altura):
        self.diametro   = diametro
        self.raio       = raio
        self.altura     = altura

    def area_base(self):
        self.areaBase = math.pi * (self.raio
                                   ** 2)
        trunc = round(self.areaBase, 2)
        print("""A área da base do cilindro corresponde a {}
 cm², ou {} PI cm²""".format(trunc, self.raio ** 2))
        return self.areaBase

    def area_lateral(self):
        self.areaLateral = 2 * (math.pi
                                * self.raio
                                * self.altura)
        trunc = round(self.areaLateral, 2)
        print("""A área lateral do cilindro corresponde a {}
 cm², ou {} PI cm²""".format(trunc,
                             2*(self.raio * self.altura)))
        return self.areaLateral

    
    def area_total(self):
        self.areaTotal = (2 * (math.pi
                               *(self.raio ** 2)
                               ) + 2 * (math.pi
                                * self.raio
                                * self.altura))
        trunc = round(self.areaTotal, 2)
        print("""A área total do cilindro corresponde a {}
 cm², ou {} PI cm²""".format(trunc, 6 * (self.raio ** 2)))
        return self.areaTotal

    def volume(self):
        self.vol = 2 * (math.pi
                           * (self.raio ** 3))
        trunc = round(self.vol, 2)
        print("""O volume do cilindro corresponde a {}
 cm³, ou {} PI cm³""".format(trunc, 2 * (self.raio ** 3)))
        return self.vol

    def imprime(self):        
        print(self.area_base())
        print(self.area_lateral())
        print(self.area_total())
        print(self.volume())

    def capacidade(self):
        print("""A capacidade do cilindro
é de {} mL""".format(round(self.volume, 2)))
        
        

def cria_cilindro():
    flag = 1
    lista_cilindros = []
    while flag:
        print("""Para todas as informações a seguir,
caso não possuir o dado, inserir 0!!\n\n""")
        diametro = float(input("""Digite o diâmetro do cilindro: """))
        if diametro <= 0:
            raio = float(input("""Digite o raio do cilindro: """))
            diametro = 2 * raio
        else:
            raio = diametro / 2
        if raio:
            altura = 2 * raio
        else:
            altura = float(input("""Digite a altura do cilindro: """))
            raio = altura / 2
        flag = int(input("""Digite 0 pra sair, ou 1 para continuar: """))
        if flag == 0 and not lista_cilindros:
            cilindro = Cilindro(diametro, raio, altura)
            return cilindro
        else:
            lista_cilindros.append(Cilindro(diametro, raio, altura))
    return lista_cilindros

def lista_cilindros(lista = Cilindro(10, 5, 10)):
    if type(lista) == list:
        fim = len(lista)
        for i in range(fim):
            print("Cilindro {}".format(i + 1))
            lista[i].imprime()
        return print("\n")
    else:
        return lista.imprime()


class Paralelepipedo:
    def __init__(self, aresta_a, aresta_b, aresta_c):
        self.largura        = aresta_a
        self.comprimento    = aresta_b
        self.profundidade   = aresta_c

    def volume(self):
        self.volume = (self.largura
                       * self.comprimento
                       * self.profundidade)
        trunc = round(self.volume, 2)
        print("""O Volume do paralelepípedo é igual a {} cm³""".format(trunc))

    
class coneCortado:
    def __init__(self, raioG, raioB, altura):
        self.raioG  = raioG
        self.raioB  = raioB
        self.altura = altura

    def volume(self):
        self.volume = (
            (
                (math.pi * self.altura)/3)
            * (
                (self.raioG ** 2)
                + (self.raioG * self.raioB)
                + (self.raioB ** 2)
                )
            )
        trunc = round(self.volume, 2)
        print("""O Volume do cone cortado é igual a {} cm³""".format(trunc))
    
        
    

if __name__ == '__main__':
    raioG = 6.5 / 2
    raioB = 4 / 2
    altura = 7
    copo = coneCortado(raioG, raioB, altura)
    copo.volume()

    
