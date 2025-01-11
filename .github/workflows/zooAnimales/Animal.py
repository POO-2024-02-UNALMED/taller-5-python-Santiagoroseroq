__package__
from zooAnimales.Mamifero import Mamifero
from zooAnimales.Ave import Ave
from zooAnimales.Reptil import Reptil
from zooAnimales.Pez import Pez
from zooAnimales.Anfibio import Anfibio
class Animal:
    totalAnimales = 0
    totalPorTipo = {
        "Mamíferos": 0,
        "Aves": 0,
        "Reptiles": 0,
        "Peces": 0,
        "Anfibios": 0
    }

    def __init__(self, nombre, edad, habitat, genero, zona=None):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero
        self.zona = zona
        Animal.totalAnimales += 1

    def movimiento(self):
        return "desplazarse"

    @classmethod
    def totalPorTipo(cls):
        resultado = ""
        for tipo, cantidad in cls.totalPorTipo.items():
            resultado += f"• {tipo}: {cantidad}\n"
        return resultado

    def __str__(self):
        if self.zona:
            return f"Mi nombre es {self.nombre}, tengo una edad de {self.edad}, habito en {self.habitat} y mi género es {self.genero}, la zona en la que me ubico es {self.zona.nombre}, en el {self.zona.zoo.nombre}."
        else:
            return f"Mi nombre es {self.nombre}, tengo una edad de {self.edad}, habito en {self.habitat} y mi género es {self.genero}."