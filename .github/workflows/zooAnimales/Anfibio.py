# zooAnimales/anfibio.py

from zooAnimales.animal import Animal

class Anfibio(Animal):
    ranas = 0
    salamandras = 0

    def __init__(self, nombre, edad, genero, colorPiel, venenoso, habitat, zona=None, zoo=None):
        super().__init__(nombre, edad, genero, zona, zoo)
        self.colorPiel = colorPiel
        self.venenoso = venenoso
        self.habitat = habitat

    def crearRana(self, nombre, edad, genero):
        self.ranas += 1
        return Anfibio(nombre, edad, genero, "rojo", True, "selva")

    def crearSalamandra(self, nombre, edad, genero):
        self.salamandras += 1
        return Anfibio(nombre, edad, genero, "negro y amarillo", False, "selva")

    def cantidadAnfibios(self):
        return Anfibio.ranas + Anfibio.salamandras

    def movimiento(self):
        return "saltar"
