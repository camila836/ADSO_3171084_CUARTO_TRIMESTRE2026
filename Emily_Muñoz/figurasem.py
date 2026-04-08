from abc import ABC, abstractmethod

# Creamos la clase abstracta
class Figura(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

# Creamos subclases concretas
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.1416 * (self.radio ** 2)

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return 0.5 * self.base * self.altura

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

class Cubo(Figura):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return 6 * (self.lado ** 2)

class Cilindro(Figura):
    def __init__(self, radio, altura):
        self.radio = radio
        self.altura = altura

    def calcular_area(self):
        return 2 * 3.1416 * self.radio * (self.radio + self.altura)

def mostrar_area(figura: Figura):
    print(f"Area: {figura.calcular_area():.2f}")

# Ejecución del programa
def main():
  circulo1 = Circulo(5)
  mostrar_area(circulo1)

  triangulo1 = Triangulo(base=4, altura=6)
  mostrar_area(triangulo1)

  rectangulo1 = Rectangulo(base=5, altura=8)
  mostrar_area(rectangulo1)

  cubo1 = Cubo(lado=3)
  mostrar_area(cubo1)

  cilindro1 = Cilindro(radio=2, altura=7)
  mostrar_area(cilindro1)


if __name__ == "__main__":
         main()