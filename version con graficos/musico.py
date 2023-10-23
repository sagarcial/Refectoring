import tkinter as tk

class MusicoGUI:
    def __init__(self, musico):
        self.musico = musico
        self.ventana = tk.Tk()
        self.ventana.title("Información del Músico")
        self.etiqueta = tk.Label(self.ventana, text="Nombre del Músico: " + self.musico.nombre)
        self.etiqueta.pack()
        self.btn_tocar = tk.Button(self.ventana, text="Tocar", command=self.tocar_instrumento)
        self.btn_tocar.pack()
        self.btn_afinar = tk.Button(self.ventana, text="Afinar Instrumento", command=self.afinar_instrumento)
        self.btn_afinar.pack()

    def tocar_instrumento(self):
        self.musico.tocar()

    def afinar_instrumento(self):
        self.musico.afinar_instrumento()

    def run(self):
        self.ventana.mainloop()
