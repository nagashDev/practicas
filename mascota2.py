ESTADOS = {
    'feliz': """
 ╔╦═══╦╗
 ║ ^ᴥ^ ║
 ╚╦═══╦╝
  ˶   ˵
""",
    'cansada': """
 ╔╦═══╦╗
 ║ TᴥT ║
 ╚╦═══╦╝
  ˶   ˵
""",
    'debil': """
 ╔╦═══╦╗
 ║ xᴥx ║
 ╚╦═══╦╝
  ︶   ︶
""",
    'comiendo': """
 ╔╦═══╦╗
 ║ •ᴥ• ║
 ╚╦═╦═╦╝
  ˶🍗˵
""",
    'durmiendo': """
 ╔╦═══╦╗
 ║ -ᴥ- ║
 ╚╦═══╦╝
  ˶ Z˵
""",
    'durmiendo_lateral': """
 ╔╦═══╦╗
 ║ ᴥ-  ║
 ╚╦═══╦╝
  ˶Zzz˵
""",
    'carcajada': """
 ╔╦═══╦╗
 ║ ᴼᴥᴼ ║
 ╚╦═══╦╝
  ˶😂˵
""",
    'full_energia': """
 ╔╦═══╦╗
 ║ ⚡ ║
 ╚╦═══╦╝
  ˶   ˵
""",
    'llena': """
 ╔╦═══╦╗
 ║ ◡ᴥ◡║
 ╚╦═╦═╦╝
  ˶🍖˵
""",
    'triste': """
 ╔╦═══╦╗
 ║ ;ᴥ; ║
 ╚╦═══╦╝
  ˶   ˵
""",
    'jugando': """
 ╔╦═══╦╗
 ║ >ᴥ< ║
 ╚╦═══╦╝
  ˶🪀˵
"""
}

class Mascota:
     
    def __init__(self,nombre,nivel_energia=100):
        self.nombre = nombre
        self.nivel_energia = nivel_energia

    def alimentar(self):
        self.nivel_energia += 20
        if self.nivel_energia > 100:
            print(f"{self.nombre} Dice: Estoy sobrecargada, mucha comida! ")
            self.nivel_energia = 100 
            print(ESTADOS['llena'])
            print(barra_energia(self.nivel_energia))
        else:
            print(f"{self.nombre} Dice: Comí bien y mi energia es de {self.nivel_energia}")
            print(ESTADOS['comiendo'])
            print(barra_energia(self.nivel_energia))
            

    def jugar(self):
        print(f"{self.nombre} Dice: Estoy jugando...")
        self.nivel_energia -= 30
        
        
        if self.nivel_energia <= 0:
            self.nivel_energia = 0
            print(f"{self.nombre} Dice: Estoy debilitada")
            print(ESTADOS['debil'])
            print(barra_energia(self.nivel_energia))
        else:
            print(f"{self.nombre} Dice: Ya jugé y mi energia es de {self.nivel_energia}")
            print(ESTADOS['jugando'])
            print(barra_energia(self.nivel_energia))

    def descansar(self):
        if self.nivel_energia < 100:
            print("Es hora de una buena siesta para recargar energia")
            self.nivel_energia += 10
            print(ESTADOS['durmiendo_lateral'])
            print(barra_energia(self.nivel_energia))

            if self.nivel_energia >= 100:
                self.nivel_energia = 100
                print(f"{self.nombre} Dice: Ahora tengo mi energía al máximo ⚡")
                print(ESTADOS['feliz'])
                print(barra_energia(self.nivel_energia))
            else:
                print(f"{self.nombre} Dice: He descansado y mi poder está ahora en {self.nivel_energia}")
                print(ESTADOS['feliz'])
                print(barra_energia(self.nivel_energia))
        else:
            print(f"{self.nombre} Dice: No necesito descanso, estoy al 100% ⚡")
            print(ESTADOS['full_energia'])
            print(barra_energia(self.nivel_energia))
                
    
    def mostrar_estado(self):
        print(f"Estado de: {self.nombre}")
        print(f"Y mi energia está: {self.nivel_energia}")
        print(barra_energia(self.nivel_energia))
        print(ESTADOS['feliz'])

        if self.nivel_energia == 100:
            print("Mi energia está al máximo")
            print(barra_energia(self.nivel_energia))
        elif self.nivel_energia >= 60:
            print("Puedo seguir jugando")
            print(barra_energia(self.nivel_energia))
        elif self.nivel_energia >= 30:
            print("Estoy cansada 😓 debería descansar pronto")
            print(barra_energia(self.nivel_energia))
        else:
            print("Estoy débil 😴 necesito dormir o comer algo")
            print(barra_energia(self.nivel_energia))
  
def rellenar_espacios(texto, tamanio):
    cantidad_espacios = tamanio - len(texto)
    return texto + ' ' * cantidad_espacios

def barra_energia(nivel, maximo=100, longitud=10):
    porcentaje = nivel / maximo
    lleno = int(porcentaje * longitud)
    vacio = longitud - lleno
    
    if porcentaje >= 0.7:
        simbolo = '█|'
        color_emoji = '🟢'
    elif porcentaje >= 0.4:
        simbolo = '█|'
        color_emoji = '🟡'
    else:
        simbolo = '█|'
        color_emoji = '🔴'
    
    barra = f"{color_emoji} [{simbolo * lleno}{'░' * vacio}] {nivel}%"
    return barra

print("╔" + "═" * 64 + "╗")
print("║" + "Bienvenido al mundo de Daksa Games".center(64) + "║")
print("╠" + "═" * 64 + "╣")
print("║" + "Ponme un nombre:".center(64) + "║")
print("╚" + "═" * 64 + "╝")

# Ahora el input ya fuera del marco
nombre = input("👉 Algo creativo por favor : ").strip()
while not nombre:
    print("⚠️ El nombre no puede estar vacío!")
    nombre = input("👉 Algo creativo por favor : ").strip()
mascota = Mascota(nombre)


print("╠" + "═" * 64 + "╣")
print("║" + f"{mascota.nombre} Ha cobrado vida!- Energia: {mascota.nivel_energia}".center(64) + "║")
print("╚" + "═" * 64 + "╝\n")

while True:

    print("╔" + "═" * 64 + "╗")
    print("║" + 'Seleccione una de las siguientes opciones'.center(64) + "║")
    print("╠" + "═" * 64 + "╣")
    print("║" + rellenar_espacios(' 1. Alimentame', 64) + "║")
    print("║" + rellenar_espacios(' 2. Dejame Jugar', 64) + "║")
    print("║" + rellenar_espacios(' 3. Quiero Descanso', 64) + "║")
    print("║" + rellenar_espacios(' 4. Cual es mi estado', 64) + "║")
    print("║" + rellenar_espacios(' 5. Salir', 64) + "║")
    print("╚" + "═" * 64 + "╝\n")
 
    opcion_seleccionada = input('Que opcion quieres: ').strip()
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
        print("Opción no valida, intenta de nuevo.")

print()