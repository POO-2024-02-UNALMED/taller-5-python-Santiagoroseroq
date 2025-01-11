__package__
from zooAnimales.animal import Animal

class Reptil(Animal):
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre, edad, genero, colorEscamas, largoCola, habitat, zona=None, zoo=None):
        super().__init__(nombre, edad, genero, zona, zoo)
        self.colorEscamas = colorEscamas
        self.largoCola = largoCola
        self.habitat = habitat

    def crearIguana(self, nombre, edad, genero):
        self.iguanas += 1
        return Reptil(nombre, edad, genero, "verde", 3, "humedal")

    def crearSerpiente(self, nombre, edad, genero):
        self.serpientes += 1
        return Reptil(nombre, edad, genero, "blanco", 1, "jungla")

    def cantidadReptiles(self):
        return Reptil.iguanas + Reptil.serpientes

    def movimiento(self):
        return "reptar"
