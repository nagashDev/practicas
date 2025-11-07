# Crea una clase SensorTemperatura que tenga:

# Atributos:
# ubicacion
# temperatura_actual (inicia en 20)
# temp_min (15)
# temp_max (30)

# Método: actualizar_temperatura(nueva_temp) que actualice la temperatura
# Método: verificar_alerta() que retorne:

# "ALTA" si temperatura > temp_max
# "BAJA" si temperatura < temp_min
# "NORMAL" si está en rango


# Método: mostrar_lectura() que muestre ubicación, temperatura y estado de alerta
# Prueba: Crea un sensor, actualiza a 35°, verifica alerta y muestra lectura


# 💡 Pistas:

# Este ejercicio es más directo que el anterior
# Solo comparas números (sin lógica booleana compleja)
class SensorTemperatura:
    
    def __init__(self,ubicacion,temp_actual=20,temp_min=15,temp_max=30):
        self.ubicacion = ubicacion
        self.temp_actual = temp_actual
        self.temp_min = temp_min
        self.temp_max = temp_max
    
    def actualizar_temperatura(self,nueva_temp):
        self.temp_actual  = nueva_temp
        print (f"Temp Actualizada a {self.temp_actual}")

    def verificar_alerta(self):
        # alta
        if self.temp_actual > self.temp_max:
            return ("ALTA")
        
        if self.temp_actual < self.temp_min:
                return ("BAJA")
        
        return ("NORMAL")
    
    def mostrar_lectura(self):
         print ("**** SENSORES ALMATEMP - COLOMBIA")
         print (f"Ubicacion : {self.ubicacion}")
         print (f"Temperatura: {self.temp_actual}")
         return self.verificar_alerta()
    
                
sensor = SensorTemperatura("Laboratorio")
sensor.actualizar_temperatura(1)
sensor.verificar_alerta()
alerta = sensor.mostrar_lectura()
print (f"Mostrar Lectura: {alerta}")