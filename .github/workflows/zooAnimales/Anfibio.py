__package__
from zooAnimales.animal import Animal

class Anfibio(Animal):
    ranas = 0
    salamandras = 0
    listado = []

    def __init__(self, nombre, edad, genero, colorPiel, venenoso, habitat, zona=None, zoo=None):
        super().__init__(nombre, edad, genero, zona, zoo)
        self.colorPiel = colorPiel
        self.venenoso = venenoso
        self.habitat = habitat
        self.listado.append(self)

    @classmethod
    def crearRana(cls, nombre, edad, genero, zona=None, zoo=None):
        cls.ranas += 1
        return cls(nombre, edad, genero, "rojo", True, "selva", zona, zoo)

    @classmethod
    def crearSalamandra(cls, nombre, edad, genero, zona=None, zoo=None):
        cls.salamandras += 1
        return cls(nombre, edad, genero, "negro y amarillo", False, "selva", zona, zoo)

    @classmethod
    def cantidadAnfibios(cls):
        return len(cls.listado)

    def movimiento(self):
        return "saltar"