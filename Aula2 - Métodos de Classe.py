def main():
    carro1 = Carro('brasilia',1968,'amarela',80)
    carro2 = Carro('fuscão',1981,'preto',95)

    carro1.acelere(40)
    carro2.acelere(50)
    carro1.acelere(80)
    carro1.pare()
    carro2.acelere(100)

class Carro:
    def __init__(self, modelo, ano, cor, velMax):
        self.modelo = modelo
        self.ano    = ano
        self.cor    = cor
        self.vel    = 0
        self.velMax = velMax
"""Aqui abaixo começam os métodos de objeto
    note que os métodos funcionam como as funções,
    e podem receber parametros para serem trabalhados dentro do código"""
    def imprima(self):
        if self.vel == 0:
            print("%s %s %d"%(self.modelo, self.cor, self.ano))
        elif self.vel < self.velMax:
            print("%s %s indo a %d Km/h"%(self.modelo, self.cor, self.vel))
        else:
            print("%s %s indo muito raaaaaapiiiiiiiiiiiiiiidooooooo!!!"%(
                self.modelo, self.cor))
    def acelere(self, vel):
        self.vel = vel
        if self.vel > self.velMax:
            self.vel = self.velMax
        self.imprima()
    def pare(self):
        self.vel = 0
        self.imprima()

        
            
