import tkinter as tk
from musico import Musico
from instrumento import Instrumento
from random import choice, randint

class Banda:
    def __init__(self, nombre, instrumentos):
        self.nombre = nombre
        self.integrantes = []
        self.instrumentos = instrumentos
        self.ventana = tk.Tk()
        self.ventana.title("Gestor de Banda")
        self.etiqueta = tk.Label(self.ventana, text="Nombre de la banda: " + self.nombre)
        self.etiqueta.pack()
        self.btn_crear = tk.Button(self.ventana, text="Crear Integrantes", command=self.crear)
        self.btn_crear.pack()
        self.btn_afinar = tk.Button(self.ventana, text="Afinar Instrumentos", command=self.afinar_instrumentos)
        self.btn_afinar.pack()
        self.btn_consultar = tk.Button(self.ventana, text="Consultar Banda", command=self.consultar)
        self.btn_consultar.pack()

    def crear(self):
        for i in range(0, randint(1, 5)):
            instrumento_random = choice(self.instrumentos)
            musico = Musico("Musico"+str(i+1), instrumento_random)
            self.integrantes.append(musico)

    def afinar_instrumentos(self):
        for musico in self.integrantes:
            musico.afinar_instrumento()

    def consultar(self):
        consulta = "Nombre de la banda: " + self.nombre + "\n"
        consulta += "Instrumentos en la banda: " + ", ".join([instrumento.nombre for instrumento in self.instrumentos]) + "\n"
        consulta += "Integrantes de la banda:\n"
        for musico in self.integrantes:
            consulta += musico.nombre + " toca " + musico.instrumento_toca.nombre + "\n"
        tk.messagebox.showinfo("Información de la Banda", consulta)

    def run(self):
        self.ventana.mainloop()