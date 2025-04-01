import math

class Circulo:
    def __init__(self, centro, raio):
        self.centro = centro  # Tupla (a, b)
        self.raio = raio
    
    def area(self):
        return math.pi * self.raio ** 2
    
    def perimetro(self):
        return 2 * math.pi * self.raio
    
    def test_pertencente(self, ponto):
        x_ponto, y_ponto = ponto
        x_centro, y_centro = self.centro
        

        distancia_quad = (x_ponto - x_centro)**2 + (y_ponto - y_centro)**2
        return distancia_quad <= self.raio**2
    
    def __str__(self):
        return f"P={self.perimetro()}, \nA={self.area()}"

if __name__ == "__main__":
    c1 = Circulo((2, 2), 3)
    print(c1)
    print(c1.test_pertencente((0, 0)))
    print(c1.test_pertencente((0, -1)))
