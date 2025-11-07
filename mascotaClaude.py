class Mascota:

    def __init__(self,nombre,tipo,edad,hambre = 50):
        self.nombre = nombre
        self.tipo = tipo
        self.edad = edad
        self.hambre = hambre

    def alimentar(self):
        self.hambre -= 20
        if self.hambre < 0:
            self.hambre = 0
        print(f"Se ha alimentado la mascota")

    def jugar(self):
        self.hambre += 15
        print(f"La mascota jugó mucho")

    def estado(self):
        print(f"Tu mascota {self.nombre} tiene un nivel de hambre: {self.hambre}")

mascotita = Mascota("Cucarron","Perro",2)
mascotita.jugar()
mascotita.jugar()
mascotita.estado()
        
        