# EJERCICIO DESAFÍO: CLASE CONTADOR
# Crea una clase Contador con:
# - Atributo: valor (inicia en 0)
# - Método: incrementar() suma 1
# - Método: decrementar() resta 1
# - Método: resetear() vuelve a 0
# - Método: mostrar() muestra el valor actual

class Contador:

    # constructor
    def __init__(self, valor = 0):
        self.valor = valor
    
    # metodos
    def incrementar(self):
        self.valor += 1
       
    def decrementar(self):
        self.valor -= 1
        
    def resetear(self):
        self.valor = 0
       
    def mostrar(self):
        print(f"El valor actual es {self.valor}")


contador = Contador()
contador.incrementar()
contador.incrementar()
contador.mostrar()
contador.resetear()
contador.decrementar()
contador.mostrar()