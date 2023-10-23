import tkinter as tk
from banda import Banda
from instrumento import Piano, Guitarra, Saxofon, Bajo, Flauta

class BandaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Banda")

        # Crear una banda con algunos instrumentos
        self.banda = Banda("Los Rítmicos", [Piano(), Guitarra(), Saxofon(), Bajo(), Flauta()])
        self.banda.crear()

        # Botones para las acciones
        self.btn_consultar = tk.Button(root, text="Consultar Información", command=self.consultar_info)
        self.btn_consultar.pack()

        self.btn_afinar = tk.Button(root, text="Afinar Instrumentos", command=self.afinar_instrumentos)
        self.btn_afinar.pack()

        self.btn_tocar = tk.Button(root, text="Tocar Sonidos de la Banda", command=self.tocar_sonidos)
        self.btn_tocar.pack()

    def consultar_info(self):
        info = self.banda.consultar()
        tk.messagebox.showinfo("Información de la Banda", info)

    def afinar_instrumentos(self):
        self.banda.afinar_instrumentos()
        tk.messagebox.showinfo("Afinación Completa", "Los instrumentos de la banda han sido afinados.")

    def tocar_sonidos(self):
        sonidos = ["¡plink plink!", "¡strum strum!", "¡jazz jazz!", "¡dum dum!", "¡flauta flauta!"]
        tk.messagebox.showinfo("Tocando Sonidos", "\n".join(sonidos))

if __name__ == "__main__":
    root = tk.Tk()
    app = BandaApp(root)
    root.mainloop()
