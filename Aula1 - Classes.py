#POO - PROGRAMAÇÃO ORIENTADA A OBJETOS

""" Objetos = dados + código
     - encapsulamento

    *Classes = tipos de objetos

    *Dados = Atributos
    *Código = Métodos
    *Os objetos são chamados de instâncias das classes"""


class Carro:
    #Construtor de classe    
    def __init__(self, modelo, ano, cor):
        """O método especial __init__
    * Conhecido como construtor da classe
    * Chamado automaticamente pelo iterpretador quando os objetos são criados
ou seja, quando as classes são instanciadas.
    """
        self.modelo = modelo
        self.ano    = ano
        self.cor    = cor
    pass
    
#Atributos I

meu_carro = Carro() #Nova instância
meu_carro.ano = 1968
meu_carro.modelo = 'Fusca'
meu_carro.cor = 'Azul'

#Atributos II - COM MÉTODO INIT

carro_ime = Carro('Brasilia',1981,'Amarelo')
#O mesmo que...
"""carro_ime.ano = 1981
carro_ime.modelo = 'Brasilia'
carro_ime.cor = 'Amarelo'"""



