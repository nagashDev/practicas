class Tarea:

    def __init__(self,descripcion,completada=False):
        self.descripcion = descripcion
        self.completada = completada
    
    def completar(self):
        self.completada = True
    
    def mostrar(self):
        print(f"Descripcion: {self.descripcion}")
        print(f"¿Completada: {'Si' if self.completada else 'No'}")
    
# 3 tareas, completo 2 y muestro todas

tarea1 = Tarea("Despertar 8 am, reunion")
tarea2 = Tarea("Gym Fisic Hard, 9 am")
tarea3 = Tarea("Salida comida, 10 am")

tarea1.completar()
tarea2.completar()

tarea1.mostrar()
tarea2.mostrar()
tarea3.mostrar()
