import tkinter as tk

class InstrumentoGUI:
    def __init__(self, instrumento):
        self.instrumento = instrumento
        self.ventana = tk.Tk()
        self.ventana.title("Información del Instrumento")
        self.etiqueta = tk.Label(self.ventana, text="Nombre del Instrumento: " + self.instrumento.nombre)
        self.etiqueta.pack()
        self.btn_afinar = tk.Button(self.ventana, text="Afinar", command=self.afinar_instrumento)
        self.btn_afinar.pack()
        self.btn_consultar = tk.Button(self.ventana, text="Consultar", command=self.consultar)
        self.btn_consultar.pack()

    def afinar_instrumento(self):
        self.instrumento.afinar()

    def consultar(self):
        consulta = "Nombre del instrumento: " + self.instrumento.nombre + "\n"
        consulta += "Puede afinar: " + ("Sí" if self.instrumento.puede_afinar else "No") + "\n"
        tk.messagebox.showinfo("Información del Instrumento", consulta)

    def run(self):
        self.ventana.mainloop()
