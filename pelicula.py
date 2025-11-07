class Pelicula:

    # constructor
    def __init__(self, titulo, director, duracion):
        self.titulo = titulo
        self.director = director
        self.duracion = duracion
        self.visto = False  # ← Este NO es parámetro, siempre False

    # metodo marcar_como_vista()
    def marcar_como_vista(self):
        self.visto = True

    # metodo mostrar_info()
    def mostrar_info(self):
        print(f"Pelicula: {self.titulo}")
        print(f"Director: {self.director}")
        print(f"Duracion: {self.duracion} min")
        # operador ternario
        print(f"¿Vista?: {'Sí' if self.visto else 'No'}")
       

# Crear películas (1 línea cada una)
print("-----------------------------------------------------")
peli1 = Pelicula("Terminator", "James Cameron", 107)
peli1.marcar_como_vista()
peli1.mostrar_info()
print("-----------------------------------------------------")
peli2 = Pelicula("Titanic", "James Cameron", 194)
peli2.mostrar_info()
print("-----------------------------------------------------")