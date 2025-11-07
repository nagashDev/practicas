# Crea una clase PuertaInteligente que tenga:

# Atributos:

# ubicacion
# cerrada (booleano, inicia en True)
# intentos_fallidos (inicia en 0)


# Método: abrir(codigo) que abra la puerta si el código es 9876, sino aumenta intentos_fallidos
# Método: cerrar() que cierre la puerta y resetee intentos_fallidos a 0
# Método: estado() que muestre si está abierta/cerrada y los intentos fallidos
# Método: bloqueada() que retorne True si intentos_fallidos >= 3
# Prueba: Intenta abrir 3 veces con código incorrecto, verifica si está bloqueada


# 💡 Pistas:

# El método abrir() debe verificar primero si está bloqueada y si ya está bloqueada, no debe permitir más intentos

class PuertaInteligente:

    # constructor
    def __init__(self, ubicacion,cerrada=True,intentos_fallidos =0,codigo = 9876):
        self.ubicacion = ubicacion
        self.cerrada = cerrada
        self.intentos_fallidos = intentos_fallidos
        self.codigo = codigo

    # metodos 

    def abrir(self, codigo):
    # 1. Verificar si está bloqueada
        if self.intentos_fallidos >= 3:
            print("🔒 Puerta BLOQUEADA. Demasiados intentos fallidos")
            return
    
    # 2. Verificar código
        if codigo == self.codigo:
            self.cerrada = False
            self.intentos_fallidos = 0  # Reset al abrir exitosamente
            print("✅ Puerta abierta correctamente")
        else:
            self.intentos_fallidos += 1
            print(f"❌ Código incorrecto. Intentos fallidos: {self.intentos_fallidos}")
        
    
    def cerrar(self):
        self.cerrada = True
        self.intentos_fallidos = 0
        print(f"La puerta sido cerrada. Reset intentos: {self.intentos_fallidos}")
    

    def estado(self):
        print(f"Verificando Estado Sistema K-Tronik de Puerta:")
        print(f"Puerta: Cerrada" if self.cerrada else "Puerta: Abierta")
        print(f"Intentos fallidos de Apertura: {self.intentos_fallidos}")
    
    def bloqueada(self):
        return self.intentos_fallidos >= 3


# Prueba: Intenta abrir 3 veces con código incorrecto, verifica si está bloqueada

puerta = PuertaInteligente("Bodega")
puerta.abrir(9876)
puerta.abrir(1111)
puerta.bloqueada()
puerta.estado()
