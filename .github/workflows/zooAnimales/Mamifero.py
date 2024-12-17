# zooAnimales/mamifero.py

from zooAnimales.Animal import Animal

class Mamifero(Animal):
    caballos = 0
    leones = 0

    def __init__(self, nombre, edad, genero, pelaje, patas, habitat, zona=None, zoo=None):
        super().__init__(nombre, edad, genero, zona, zoo)
        self.pelaje = pelaje
        self.patas = patas
        self.habitat = habitat

    def crearCaballo(self, nombre, edad, genero):
        self.caballos += 1
        return Mamifero(nombre, edad, genero, True, 4, "pradera")

    def crearLeon(self, nombre, edad, genero):
        self.leones += 1
        return Mamifero(nombre, edad, genero, True, 4, "selva")

    def cantidadMamiferos(self):
        return Mamifero.caballos + Mamifero.leones

    def movimiento(self):
        return "caminar"
