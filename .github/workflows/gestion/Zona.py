__package__ 
class Zona:
    def __init__(self, nombre, habitat):
        self.nombre = nombre
        self.habitat = habitat
        self.animales = []

    def agregarAnimales(self, animal):
        self.animales.append(animal)

    def cantidadAnimales(self):
        return len(self.animales)

    def __str__(self):
        return f"Zona: {self.nombre}, Habitat: {self.habitat}"

