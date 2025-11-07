
## EJERCICIO 3: Clase Cuenta Bancaria
# Crea una clase `CuentaBancaria` que tenga:
# - **Atributos**: titular, saldo (que inicie en 0)
# - **Método**: `depositar(monto)` que agregue dinero al saldo
# - **Método**: `retirar(monto)` que quite dinero (solo si hay suficiente saldo)
# - **Método**: `mostrar_saldo()` que muestre el saldo actual
# - **Prueba**: Crea una cuenta, deposita $1000, retira $300 y muestra el saldo

class CuentaBancaria:
    
    # constructor
    def __init__(self,titular,saldo=0):
        self.titular = titular
        self.saldo = saldo

    # metodo
    def depositar(self,monto):
        self.saldo += monto
        print(f"Deposito Exitoso, Saldo {self.saldo}")

    def retirar(self,retiro):
        if retiro <= self.saldo:
            self.saldo -= retiro
            print(f"Has retirado: {retiro}, Saldo {self.saldo}")
        else:
            print("NO SE PUEDE EJECUTAR LA TRANSACCION")

    def mostrar_saldo(self):
        print(f"Tu saldo actual es: {self.saldo}")


titular = input("Titular de la cuenta: ")
nuevaCuenta = CuentaBancaria(titular)
deposito = float(input("Ingresa el valor del deposito: "))
nuevaCuenta.depositar(deposito)
retiro = float(input("Cuanto deseas retirar: "))
nuevaCuenta.retirar(retiro)
nuevaCuenta.mostrar_saldo()