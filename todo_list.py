## EJERCICIO 9: Clase Tarea (TODO List)
# Crea una clase `Tarea` que tenga:
# - **Atributos**: descripcion, completada (inicia en False)
# - **Método**: `completar()` que marque la tarea como completada
# - **Método**: `mostrar()` que imprima la descripción y si está completada
# - **Prueba**: Crea 3 tareas, completa 2 de ellas y muestra todas

# ---

class Tarea:

    # constructor
    def __init__(self, descripcion,completada = False):
        self.descripcion = descripcion
        self.completada = completada

    # metodo
    def completar(self):
        self.completada = True

    def mostrar(self):
        if self.completada == True:
            estado = "Completada"
        else:
            estado = "Pendiente"
        print(f"Tarea: {self.descripcion} | Estado: {estado}")

# instancia

tarea1 = Tarea("Reunion por meet........08:00 AM")
tarea2 = Tarea("Compras Tienda Uva 9....09:00 AM")
tarea3 = Tarea("Almuerzo Gerente........11:30 AM")

tarea1.completar()
tarea2.completar()

tarea1.mostrar()
tarea2.mostrar()
tarea3.mostrar()

