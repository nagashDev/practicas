# ## EJERCICIO 8: Clase Mascota
# Crea una clase `Mascota` que tenga:
# - **Atributos**: nombre, tipo (perro, gato, etc.), edad, hambre (inicia en 50)
# - **Método**: `alimentar()` que reduzca el hambre en 20 (mínimo 0)
# - **Método**: `jugar()` que aumente el hambre en 15
# - **Método**: `estado()` que muestre el nombre y nivel de hambre
# - **Prueba**: Crea una mascota, juega 2 veces, aliméntala y muestra su estado

# ---
class Mascota:

    # Metodo Constructor
    def __init__(self,nombre,tipo,edad, hambre =50):
        self.nombre = nombre
        self.tipo = tipo
        self.edad = edad
        self.hambre = hambre

    # Metodos

    def alimentar(self):
        self.hambre = max(0, self.hambre - 20)
    
    def jugar(self):
        self.hambre = min(100, self.hambre +15)

    def estado(self):
        print(f"Tu mascota {self.nombre} tiene hambre del {self.hambre}")

mascota = Mascota("Tamagochi","Perro",2)
mascota.alimentar()
mascota.jugar()
mascota.jugar()
mascota.estado()