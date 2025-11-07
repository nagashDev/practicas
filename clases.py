class Telefono:
    numero = None
    marca = None
    modelo = None
    imei = None

    def llamar(self, numero):
        print(f"Llamada saliente")
        print(f"Desde el numero {self.numero}")
        print(f"Desde el modelo {self.modelo}")
        print(f"Llamando al numero {numero}")

    def informacion(self):
        print("-------------------------------")
        print(self.numero)
        print(self.marca)
        print(self.modelo)
        print(self.ime)
        print("-------------------------------")

samsung = Telefono()
samsung.numero = "3219751488"
samsung.modelo = "A32"
samsung.marca = "Samsung"
samsung.ime = "454656546456456456456"

iphone = Telefono()
iphone.numero = "3235677488"
iphone.modelo = "16 Pro Max"
iphone.marca = "Iphone"
iphone.ime = "45656546dfdfdfd456456456"

print(samsung.modelo)
print(iphone.modelo)


samsung.informacion()
iphone.informacion()





