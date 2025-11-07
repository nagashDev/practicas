print("╔" + "═" * 64 + "╗")
print("║" + "Ejercicio Clase Perro POO".center(64) + "║")
print("╚" + "═" * 64 + "╝\n")
# crear un constructor para inicializar 
# crear metodo ladrar y Presentarse
# crear objetos (instanciar)

class Perro:

    def __init__(self,nombre,raza,edad,energia):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.energia = 90

    def ladrar(self):
        return f"{self.nombre} dice: Guau Guau!"

    def presentarse(self):
        return f"Me llamo {self.nombre}, mi raza es {self.raza} y tengo {self.edad} de edad"
    
    def alimentarse(self):
        return f"{self.nombre} te da las gracias por el alimento. Mi energia es {self.energia + 10}"

# perro1 = Perro("Cucarron","Labrador",3,10)
# perro2 = Perro("Pipo","Criollo",5,10)

# print("Perro1: ")
# print(perro1.presentarse())

# print("Perro 2: ")
# print(perro2.ladrar())


nombrePerro = input("Nombre de perro: ")
razaPerro = input("Raza: ")
edadPerro = input("Edad: ")
energiaPerro = input("Energia: ")


print("\n" + "╔" + "═" * 64 + "╗")
print("║" + f"Nombre: {nombrePerro}".center(64) + "║")
print("║" + f"Raza: {razaPerro}".center(64) + "║")
print("║" + f"Edad: {edadPerro}".center(64) + "║")
print("║" + f"Energia: {energiaPerro}".center(64) + "║")
print("╚" + "═" * 64 + "╝")

perro3 = Perro(nombrePerro,razaPerro,edadPerro,energiaPerro)
print("\n" + "╔" + "═" * 64 + "╗")
print("║" + perro3.presentarse().center(64) + "║")
print("║" + perro3.alimentarse().center(64) + "║")
print("╚" + "═" * 64 + "╝\n")