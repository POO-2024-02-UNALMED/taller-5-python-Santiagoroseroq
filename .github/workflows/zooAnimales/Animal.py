# zooAnimales/animal.py
from zooAnimales.Mamifero import Mamifero
from zooAnimales.Ave import Ave
from zooAnimales.Reptil import Reptil
from zooAnimales.Pez import Pez
from zooAnimales.Anfibio import Anfibio
class Animal:
    totalAnimales = 0  # Variable de clase para contar todos los animales creados.

    def __init__(self, nombre, edad, genero, zona=None, zoo=None):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.zona = zona
        self.zoo = zoo
        Animal.totalAnimales += 1  # Incrementa el contador global de animales.

    @classmethod
    def totalPorTipo(cls):
        mamiferos = Mamifero.cantidadMamiferos()
        aves = Ave.cantidadAves()
        reptiles = Reptil.cantidadReptiles()
        peces = Pez.cantidadPeces()
        anfibios = Anfibio.cantidadAnfibios()
        
        return f"Mamíferos: {mamiferos}, Aves: {aves}, Reptiles: {reptiles}, Peces: {peces}, Anfibios: {anfibios}"


    def __str__(self):
        return f"Mi nombre es {self.nombre}, tengo una edad de {self.edad}, " \
               f"habito en {self.zona}, mi género es {self.genero}, " \
               f"la zona en la que me ubico es {self.zona}, en el zoológico {self.zoo}."

    def movimiento(self):
        return "desplazarse"  # El movimiento por defecto para la clase Animal es "desplazarse".
