__package__ 

class Zona:
    def __init__(self, nombre, zoo):
        self.nombre = nombre
        self.zoo=zoo
        self.animales = []

    def agregarAnimales(self, animal):
        self.animales.append(animal)

    def cantidadAnimales(self):
        return len(self.animales)

    def __str__(self):
        return f"Zona: {self.nombre}, Habitat: {self.habitat}"

