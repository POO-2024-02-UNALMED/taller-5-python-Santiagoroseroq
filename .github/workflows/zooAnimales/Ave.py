__package__
from zooAnimales.Animal import Animal
class Ave(Animal):
    halcones = 0
    aguilas = 0
    listado = []

    def __init__(self, nombre, edad, habitat, genero, zona=None, colorPlumas=None):
        super().__init__(nombre, edad, habitat, genero, zona)
        if colorPlumas is not None:
            self.colorPlumas = colorPlumas
        self.listado.append(self)

    @classmethod
    def crearHalcon(cls, nombre, edad, genero, zona=None):
        cls.halcones += 1
        return cls(nombre, edad, "montañas", genero, zona, "café glorioso")

    @classmethod
    def crearAguila(cls, nombre, edad, genero, zona=None):
        cls.aguilas += 1
        return cls(nombre, edad, "montañas", genero, zona, "blanco y amarillo")

    @classmethod
    def cantidadAves(cls):
        return len(cls.listado)