class Triangulo:       
    def __init__(self, lado_a, lado_b, lado_c):
        self.a  = lado_a
        self.b  = lado_b
        self.c  = lado_c

    def perimetro(self):
        P = (self.a + self.b + self.c)
        return P

    def tipo_lado(self):
        lados = [self.a, self.b, self.c]
        escaleno = 0
        for i in lados:
            if lados.count(i) == 3:
                return "equilátero"
            elif lados.count(i) == 2:
                return "isósceles"
            elif lados.count(i) == 1:
                escaleno += 1
        if escaleno == 3 and not self.retangulo():            
            return "escaleno"
        if self.retangulo():
            return "retângulo"       

    def retangulo(self):        
        lados = self.ordena_lista([self.a, self.b, self.c])
        if lados[2] in self.Hipotenusa():
            if ((lados[0]**2) + (lados[1]**2)) == lados[2]**2:
                return True
            else:
                return False
        else:
            return False
        
    def ordena_lista(self, lados):
        fim = len(lados)
        for x in range (fim-1,0,-1):
            for i in range(x):
                if lados[i] > lados[i+1]:
                    lados[i], lados[i+1] = lados[i+1], lados[i]
        return lados

    def semelhantes(self, t2):
        t1 = self.ordena_lista([self.a, self.b, self.c])
        t2 = t2.ordena_lista([t2.a, t2.b, t2.c])
        k = []
        for i in range(len(t1)):
            if t1[i] >= t2[i]:
                if t1[i]%t2[i] == 0:
                    k.append(t1[i]/t2[i])
                else:
                    return False
            else:
                if t2[i]%t1[i] == 0:
                    k.append(t2[i]/t1[i])
        if k.count(k[0]) == 3:
            return True
        else:
            return False
                      
    def retHipo(self):
        if self.retangulo():
            return print(self.ordena_lista([self.a, self.b, self.c])[2])
        else:
            return ("Não tem Hipotenusa pois o triangulo é {}".format(self.tipo_lado()))
    
    def Hipotenusa(self):
        hipo = [5, 10, 13, 15, 17, 20, 25, 26,
                  29, 30, 34, 35, 37, 39, 40, 41,
                  45, 50, 51, 52, 53, 55, 58, 60,
                  61, 65, 68, 70, 73, 74, 75, 78,
                  80, 82, 85, 87, 89, 90, 91, 95,
                  97, 100, 101, 102, 104, 105, 106,
                  109, 110, 115, 116, 120, 125]
        return hipo

    
    
if __name__ == '__main__':
    t1 = Triangulo(2, 2, 2)
    t2 = Triangulo(4, 4, 4)
    print(t1.semelhantes(t2))
    t1 = Triangulo(2, 4, 6)
    t2 = Triangulo(4, 8, 12)
    print(t1.semelhantes(t2))
    t1 = Triangulo(2, 4, 6)
    t2 = Triangulo(4, 9, 10)
    print(t1.semelhantes(t2))
    t1 = Triangulo(10, 5, 2)
    t2 = Triangulo(1, 2, 5)
    print(t1.semelhantes(t2))
    
