# ## EJERCICIO 2: Sistema de Alarma 🔔
# Crea una clase `Alarma` que tenga:
# - **Atributos**: ubicacion (ej: "Sala"), activada (booleano, inicia en False), codigo (número de 4 dígitos)
# - **Método**: `activar(codigo_ingresado)` que active la alarma solo si el código es correcto
# - **Método**: `desactivar(codigo_ingresado)` que desactive solo si el código es correcto y está activada
# - **Método**: `verificar_estado()` que imprima si está activada o desactivada
# - **Prueba**: Crea una alarma con código 1234, intenta activar con código incorrecto, luego con correcto

# ---

class Alarma:

    # contructor
    def __init__(self, ubicacion,codigo,activada = False):
        self.ubicacion = ubicacion
        self.codigo = codigo
        self.activada = activada
    
    # metodo
    def activar(self,codigo_ingresado):
        if self.codigo == codigo_ingresado:
            self.activada = True
            print("Alarma Activada !")
        else:
            print("Codigo incorrecto")
            
    def desactivar(self,codigo_ingresado):
        if self.codigo == codigo_ingresado and self.activada:
            print("Alarma Desactivada")
            self.activada = False
        else:
            print("No se ha podido desactivar la alarma")

    def verificar_estado(self):
         estado = "🔴 Activada" if self.activada else "🟢 Desactivada"
         print(f"Alarma en {self.ubicacion}: {estado}")

# - **Prueba**: Crea una alarma con código 1234, intenta activar con código incorrecto, luego con correcto

alarma = Alarma("Bodega",1234)
alarma.activar(5555)
alarma.verificar_estado()
alarma.activar(1234)
alarma.verificar_estado()
