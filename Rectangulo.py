# Crea una clase Rectangulo que tenga:
# Atributos: ancho, alto
# Método: calcular_area() que retorne el área (ancho × alto)
# Método: calcular_perimetro() que retorne el perímetro 2×(ancho + alto)
# Método: es_cuadrado() que retorne True si el ancho y alto son iguales, False si no
# Prueba: Crea un rectángulo de 5×3 y muestra su área, perímetro y si es cuadrado
# Pistas:
# Los métodos deben usar return, no print
# Luego imprimes los resultados en el código principal

class Rectangulo:

    # constructor
    def __init__(self,ancho,alto):
        self.ancho = ancho
        self.alto = alto

    # metodo area 
    def calcular_area(self):
        return self.ancho * self.alto
    
      # metodo perimetro
    def calcular_perimetro(self):
        return 2 * (self.ancho + self.alto)
    
    def es_cuadrado(self):
       return self.ancho == self.alto

ancho = float(input("Ingresa Ancho: "))
alto = float(input("Ingresa Alto: "))
rectangulo1 = Rectangulo(ancho,alto)
print(rectangulo1.es_cuadrado())
print (rectangulo1.calcular_area())
print(rectangulo1.calcular_perimetro())