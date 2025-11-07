## EJERCICIO 2: Clase Estudiante
# Crea una clase `Estudiante` que tenga:
# - **Atributos**: nombre, edad, carrera
# - **Método**: `estudiar(materia)` que imprima "{nombre} está estudiando {materia}"
# - **Método**: `cumplir_años()` que aumente la edad en 1 y lo anuncie
# - **Prueba**: Crea 2 estudiantes y haz que estudien diferentes materias

class Estudiante:

    # constructor
    def __init__(self,nombre,edad,carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

    # metodos
    def estudiar_materia(self,materia):
        return f"{self.nombre} ve la materia {materia}"
    
    def cumplir_anos(self):
        self.edad += 1
        return f"La nueva edad es {self.edad}"

for i in range (2):
    nombre = input("Ingresa nombre alumno: ")
    edad = int(input("Edad del estudiante: "))
    carrera = input("Carrera: ")
    materia = input("Que materia ves: ")

    alumno = Estudiante(nombre,edad,carrera)
    print(f"El estudiante {i+1} {alumno.estudiar_materia(materia)}")
    print(alumno.cumplir_anos())