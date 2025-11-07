# ## EJERCICIO 1: Sistema de Vuelos ✈️
# Crea una clase `Vuelo` que tenga:
# - **Atributos**: numero_vuelo, destino, capacidad, pasajeros_actuales (inicia en 0)
# - **Método**: `agregar_pasajero()` que aumente pasajeros_actuales en 1 (validar que no exceda capacidad)
# - **Método**: `mostrar_info()` que muestre todos los datos y asientos disponibles
# - **Método**: `esta_lleno()` que **retorne** True si está lleno
# - **Prueba**: Crea un vuelo con capacidad 2, agrega 3 pasajeros (el 3° debe fallar) y muestra info

# ---
class Vuelo:

    # metodo constructor 
    def __init__(self, numero_vuelo,destino,capacidad,pasajeros_actuales=0):
        self.numero_vuelo = numero_vuelo
        self.destino = destino
        self.capacidad = capacidad
        self.pasajeros_actuales = pasajeros_actuales

    # metodos
    def agregar_pasajero(self):
        if self.pasajeros_actuales >= self.capacidad:
            print(f"Se excede la capacidad de {self.capacidad}")
        else:
            self.pasajeros_actuales +=1
            print(f"Pasajero agregado correctamente")

    def mostrar_info(self):
            print(f"El vuelo {self.numero_vuelo} con destino a {self.destino}")
            print(f"La capacidad del vuelo es de {self.capacidad} personas en total")
            print(f"A bordo {self.pasajeros_actuales} almas, Buen viaje!")

    def esta_lleno(self):
        if self.capacidad == self.pasajeros_actuales:
            return True
        else:
             return False

vuelo = Vuelo("AV123", "Bogotá", 2)
vuelo.agregar_pasajero()
vuelo.agregar_pasajero()
vuelo.agregar_pasajero()  #

print(f"Esta lleno? {vuelo.esta_lleno()}")
vuelo.mostrar_info()

