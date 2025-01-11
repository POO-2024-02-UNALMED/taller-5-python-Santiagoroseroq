__package__
from zooAnimales.animal import Animal

class Pez(Animal):
    salmones = 0
    bacalaos = 0
    listado = []

    def __init__(self, nombre, edad, genero, colorEscamas, cantidadAletas, habitat, zona=None, zoo=None):
        super().__init__(nombre, edad, genero, zona, zoo)
        self.colorEscamas = colorEscamas
        self.cantidadAletas = cantidadAletas
        self.habitat = habitat
        self.listado.append(self)

    @classmethod
    def crearSalmon(cls, nombre, edad, genero, zona=None, zoo=None):
        cls.salmones += 1
        return cls(nombre, edad, genero, "rojo", 6, "océano", zona, zoo)

    @classmethod
    def crearBacalao(cls, nombre, edad, genero, zona=None, zoo=None):
        cls.bacalaos += 1
        return cls(nombre, edad, genero, "gris", 6, "océano", zona, zoo)

    @classmethod
    def cantidadPeces(cls):
        return len(cls.listado)

    def movimiento(self):
        return "nadar"