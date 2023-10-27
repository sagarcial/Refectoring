from abc import ABC, abstractmethod

class Afinable(ABC):
    @abstractmethod
    def afinar(self):
        pass

class Tocable(ABC):
    @abstractmethod
    def tocar(self):
        pass

class Instrumento(Afinable, Tocable):
    def __init__(self, nombre, puede_afinar=False):
        self.nombre = nombre
        self.puede_afinar = puede_afinar

    def afinar(self):
        if self.puede_afinar:
            print(f"Afinando {self.nombre}")
        else:
            print(f"{self.nombre} no se puede afinar")

    def tocar(self):
        pass

    def consultar(self):
        print("Soy: ", self.nombre)

# Clases derivadas, como Piano, Guitarra, etc., deben implementar Afinable y Tocable
class Piano(Instrumento):
    def __init__(self):
        super().__init__("Piano")

    def tocar(self):
        print("Tocando piano: ¡plink plink!")

class Flauta(Instrumento):
    def __init__(self):
        super().__init__("Flauta")

    def tocar(self):
        print("Tocando flauta: ¡flauta flauta!")

class Guitarra(Instrumento):
    def __init__(self):
        super().__init__("Guitarra")
        self.puede_afinar = True

    def tocar(self):
        print("Tocando guitarra: ¡strum strum!")

class Saxofon(Instrumento):
    def __init__(self):
        super().__init__("Saxofon")
        self.puede_afinar = True

    def tocar(self):
        print("Tocando saxofon: ¡jazz jazz!")

class Bajo(Instrumento):
    def __init__(self):
        super().__init__("Bajo")
        self.puede_afinar = True

    def tocar(self):
        print("Tocando bajo: ¡dum dum!")
