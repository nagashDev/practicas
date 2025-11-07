#  EJERCICIO 7: Clase Calculadora
# Crea una clase Calculadora que tenga:

# Método: sumar(a, b) que retorne la suma
# Método: restar(a, b) que retorne la resta
# Método: multiplicar(a, b) que retorne la multiplicación
# Método: dividir(a, b) que retorne la división (maneja el caso de dividir por 0)
# Prueba: Crea una calculadora y realiza las 4 operaciones


# Pistas:

# La clase NO tiene constructor ni atributos
# Los métodos reciben 2 parámetros: a y b
# Para dividir por 0, usa if para validar

class Calculadora:

    def sumar(self, a, b):
        return a + b
    def restar(self, a, b):
        return a - b
    def multiplicar(self, a, b):
        return a * b
    def dividir(self, a, b):
        if b == 0:
            print("Division por cero no puede ejecutarse")
            return None
        else:
            return a / b 
        
# instanciar

calcu = Calculadora()
print("---------------------------------------------------")
print(f"Suma: {calcu.sumar(5,5)}") # 10
print(f"Resta: {calcu.restar(5,5)}") # 0
print(f"Multiplicar: {calcu.multiplicar(5,5)}") # 25
print(f"Dividir: {calcu.dividir(5,5)}") # 1
print(f"Dividir: {calcu.dividir(5,0)}") # 0 y error
print("---------------------------------------------------")
    
