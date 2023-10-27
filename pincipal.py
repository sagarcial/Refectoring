from banda import Banda
from instrumento import Piano, Guitarra, Saxofon, Bajo, Flauta

if __name__ == "__main__":
    # Crear una banda con algunos instrumentos
    b = Banda("Los Rítmicos", [Piano(), Guitarra(), Saxofon(), Bajo(), Flauta()])
    
    # Crear músicos aleatorios
    b.crear()
    
    # Consultar la información inicial de la banda
    b.consultar()
    
    # Dar la opción de afinar los instrumentos
    opcion = input("¿Deseas afinar los instrumentos de la banda? (S/N): ").strip().lower()
    b.consultar()
    print("\nTocando sonidos de la banda:\n")
    if opcion == 's':
        b.afinar_instrumentos()  # Llama al método para afinar los instrumentos
    for musico in b.integrantes:
        musico.tocar()  # Consultar la información actualizada de la banda
