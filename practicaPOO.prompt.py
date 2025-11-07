print("LEjercicios")

## EJERCICIO 1: Clase Libro
# Crea una clase `Libro` que tenga:
# - **Atributos**: titulo, autor, paginas
# - **Método**: `mostrar_info()` que imprima todos los datos del libro
# - **Prueba**: Crea 2 objetos de libros diferentes y muestra su información

# ---
print("╔" + "═" * 64 + "╗")
print("║" + "Libro".center(64) + "║")
print("╚" + "═" * 64 + "╝\n")

class Libro:

    # metodo constructor
    def __init__(self,titulo,autor,paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    
    # metodo mostrarInfo()
    def mostrar_info(self):
        return f"El libro escogido se llama {self.titulo} de {self.autor} con {self.paginas} paginas"
    
# capturo los datos
for i in range(2):
    titulo = input("Ingresa el titulo del libro: ")
    autor = input("Ingresa el autor del libro: ")
    paginas = int(input("Ingresa el numero de paginas: "))
    libro1 = Libro(titulo,autor,paginas)
    print("Datos del libro: ")
    print(libro1.mostrar_info())





