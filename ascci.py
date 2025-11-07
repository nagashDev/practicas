# -*- coding: utf-8 -*-
class Mascota:
     
    def __init__(self,nombre,nivel_energia=100):
        self.nombre = nombre
        self.nivel_energia = nivel_energia
    
    def alimentar(self):
        self.nivel_energia += 20
        if self.nivel_energia > 100:
            print(f"{self.nombre} está sobrecargada, mucha comida! AQUI VA CARA DE LLENA ")
            self.nivel_energia = 100 
        else:
            print(f"{self.nombre} comio bien y su energia es de {self.nivel_energia}")
            

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
            print("100%⚡-Energia Maxima ")
        elif self.nivel_energia >= 60:
            print("😀 puede seguir jugando")
        elif self.nivel_energia >= 30:
            print("cansada 😓 debería descansar pronto")
        else:
            print("débil 😴 necesita dormir o alimentarse")
def rellenar_espacios(texto, tamanio):
    cantidad_espacios = tamanio - len(texto)
    return texto + ' ' * cantidad_espacios

mascota = input("Dale un nombre a tu mascota: ")
mascota = Mascota(mascota)
print(f"\n✨ ¡{mascota.nombre} ha cobrado vida! ✨\n")


while True:
    print("╔" + "═" * 64 + "╗")
    print("║" + "Bienvenido al mundo de Daksa Games".center(64) + "║")
    print("╚" + "═" * 64 + "╝\n")
 
    print("╔" + "═" * 64 + "╗")
    print("║" + 'Seleccione una de las siguientes opciones'.center(64) + "║")
    print("╠" + "═" * 64 + "╣")
    print("║" + rellenar_espacios(' 1. Alimentar', 64) + "║")
    print("║" + rellenar_espacios(' 2. Jugar', 64) + "║")
    print("║" + rellenar_espacios(' 3. Descansar', 64) + "║")
    print("║" + rellenar_espacios(' 4. Mostrar estado', 64) + "║")
    print("║" + rellenar_espacios(' 5. salir', 64) + "║")
    print("╚" + "═" * 64 + "╝\n")
 
    opcion_seleccionada = input('Digite la opcion a elegir: ').strip()
    #print(opcion_seleccionada)
   
    if (opcion_seleccionada == '1'):
        mascota.alimentar()
    elif(opcion_seleccionada == '2'):
        mascota.jugar()
    elif(opcion_seleccionada == '3'):
        mascota.descansar()
    elif(opcion_seleccionada == '4'):
        mascota.mostrar_estado()
    elif (opcion_seleccionada == '5'):
        print("Gracias por jugar 🐾 ¡Hasta pronto!")
        break
    else:
        print("⚠️ Opción no valida, intenta de nuevo.")

print()




