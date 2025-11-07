# 1. Crear una clase Mascota
# La clase debe representar una mascota con las siguientes propiedades:
# nombre : el nombre de la mascota.
# energia : debe iniciar con el valor 100 por defecto

# 2. Crear los métodos de la clase
# Tu mascota debe poder realizar las siguientes acciones:
# alimentar() → aumenta la energía en +20
# jugar() → reduce la energía en −30
# descansar() → aumenta la energía en +10
# mostrar_estado() → muestra la energía actual y su estado general.

# 3. Reglas de energía
# Implementa las siguientes condiciones:
# Si la energía supera 100, la mascota está “sobrecargada” y su energía debe quedar en 100.
# Si la energía llega a 0 o menos, la mascota está “debilitada”.
# Si la mascota no puede realizar una acción, debe mostrarse un mensaje gracioso (por ejemplo, si
# intenta jugar estando cansada o comer estando llena).

class Mascota:

    # Constructor
    def __init__(self,nombre,nivel_energia=100):
        self.nombre = nombre
        self.nivel_energia = nivel_energia

    # Metodos
    def alimentar(self):
        self.nivel_energia += 20
        if self.nivel_energia > 100:
            print(f"{self.nombre} esta sobrecargada, mucha comida! AQUI VA CARA DE LLENA ")
            self.nivel_energia = 100 
        else:
            print(f"{self.nombre} comió bien y su energia es de {self.nivel_energia}")
            

    def jugar(self):
        print(f"{self.nombre} esta jugando...")
        self.nivel_energia -= 30
        
        if self.nivel_energia <= 0:
            self.nivel_energia = 0
            print(f"{self.nombre} està debilitada, necesita dormir o comer")
        else:
            print(f"Despues de jugar {self.nombre} su energia es de {self.nivel_energia}")

    def descansar(self):
        print(f"Es hora de una buena siesta para recargar energia")
        self.nivel_energia += 10

        if self.nivel_energia >= 100:
            self.nivel_energia = 100
            print(f"{self.nombre} tiene su energia maxima")
        else:
            print(f"Despues de descansar la energia està en {self.nivel_energia}")
    
    def mostrar_estado(self):
        print(f"Estado de: {self.nombre}")
        print(f"Tu nivel de energia: {self.nivel_energia}")

        if self.nivel_energia == 100:
            print(" 100%⚡")
        elif self.nivel_energia >= 60:
            print("😀 puede seguir jugando")
        elif self.nivel_energia >= 30:
            print("cansada 😓 debería descansar pronto")
        else:
            print("débil 😴 necesita dormir o alimentarse")

            

mascota = Mascota("Tamagochi")
mascota.jugar()
mascota.jugar()
mascota.jugar()
mascota.jugar()
mascota.mostrar_estado()