emociones = {
    'contento': r"""
  ╭─────────╮
  │  ^._.^  │
  │ ( 0 0 ) │
  │  \ - /  │
  ╰─────────╯
    """,
    'bajo': r"""
  ╭─────────╮
  │  - . -  │
  │ ( . . ) │
  │  /   \  │
  ╰─────────╯
    """,
    'hambriento': r"""
  ╭─────────╮
  │  >︵<   │
  │ ( • • ) │
  │  \_🍪/  │
  ╰─────────╯
    """,
    'reposo': r"""
  ╭─────────╮
  │  - - -  │
  │ (  -  ) │
  │  z z z  │
  ╰─────────╯
    """,
    'lado': r"""
  ╭─────────╮
  │ ( ͡° ͜ʖ│
  │  ͡° )   │
  │  zzz    │
  ╰─────────╯
    """,
    'maximo': r"""
  ╭─────────╮
  │  ⚡⚡⚡  │
  │ ( ^_^ ) │
  │  READY  │
  ╰─────────╯
    """
}

def rellenar_espacios(texto, tamanio):
    cantidad_espacios = tamanio - len(texto)
    return texto + ' ' * max(0, cantidad_espacios)

def porcentaje_numerico(nivel, maximo=100):
    nivel_clamped = max(0, min(maximo, int(nivel)))
    return f"Energía: {nivel_clamped}%"

class MascotaNueva:
    
    def __init__(self, nombre="Amiga"):
        self.nombre = nombre.strip() or "Amiga"
        self.nivel_energia = 100

    def alimentar(self):
        self.nivel_energia += 20
        if self.nivel_energia > 100:
            self.nivel_energia = 100
            print(f"{self.nombre} ¡Uf, demasiado! Me siento llena 🤗")
            print(emociones['maximo'])
        else:
            print(f"{self.nombre} Gracias por la comida 😝")
            print(emociones['hambriento'])
        print(porcentaje_numerico(self.nivel_energia))

    def jugar(self):
        print(f"{self.nombre} Voy a jugar un rato...🥳")
        self.nivel_energia -= 30
        if self.nivel_energia <= 0:
            self.nivel_energia = 0
            print(f"{self.nombre} dice: Me he quedado sin fuerzas...😥")
            print(emociones['bajo'])
        else:
            print(f"{self.nombre} ¡Fue divertido! 🫡")
            print(emociones['contento'])
        print(porcentaje_numerico(self.nivel_energia))

    def descansar(self):
        if self.nivel_energia < 100:
            print(f"{self.nombre} Hora de recargar...🫠")
            self.nivel_energia += 10
            if self.nivel_energia > 100:
                self.nivel_energia = 100
            if self.nivel_energia >= 90:
                print(emociones['maximo'])
            elif self.nivel_energia >= 60:
                print(emociones['contento'])
            else:
                print(emociones['reposo'])
            print(porcentaje_numerico(self.nivel_energia))
        else:
            print(f"{self.nombre} Ya estoy al 100% 🙂‍↔️")
            print(emociones['maximo'])
            print(porcentaje_numerico(self.nivel_energia))

    def mostrar_estado(self):
        print(f"--- Estado actual de {self.nombre} ---")
        print(porcentaje_numerico(self.nivel_energia))
        if self.nivel_energia == 100:
            print("Mensaje: Energía completa. ¡Perfecta para jugar!")
            print(emociones['maximo'])
        elif self.nivel_energia >= 60:
            print("Mensaje: Me siento bien.")
            print(emociones['contento'])
        elif self.nivel_energia >= 30:
            print("Mensaje: Un poco cansada, debería descansar pronto.")
            print(emociones['reposo'])
        else:
            print("Mensaje: Muy baja — necesito comida o descanso.")
            print(emociones['bajo'])

# ---------------- MENÚ INTERACTIVO ---------------- #
if __name__ == "__main__":
    print("╠" + "═" * 64 + "╣")
    print("║" + "CREACION DE MASCOTA".center(64) + "║")
    print("╚" + "═" * 64 + "╝")
    nombre = input("Mi nombre será: ").strip()
    mascota = MascotaNueva(nombre)
    while True:
        print("╔" + "═" * 64 + "╗")
        print("║" + rellenar_espacios(' 1.................Quiero comer 🥱', 64) + "║")
        print("║" + rellenar_espacios(' 2.................Juega conmigo 😋', 64) + "║")
        print("║" + rellenar_espacios(' 3.................Dormiré un rato 😴', 64) + "║")
        print("║" + rellenar_espacios(' 4.................Cómo estoy 😎', 64) + "║")
        print("║" + rellenar_espacios(' 5.................Salir 👍', 64) + "║")
        print("╚" + "═" * 64 + "╝\n")
        opcion = input('Opcion: ').strip()
        if opcion == '1':
            mascota.alimentar()
        elif opcion == '2':
            mascota.jugar()
        elif opcion == '3':
            mascota.descansar()
        elif opcion == '4':
            mascota.mostrar_estado()
        elif opcion == '5':
            print("Gracias por jugar 🥰")
            break
        else:
            print("Opción no válida, intenta de nuevo 😵")
