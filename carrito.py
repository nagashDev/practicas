# Crea una clase `CarritoCompras` que tenga:

# - **Atributos**: 
#   - `producto1_nombre`, `producto1_precio`
#   - `producto2_nombre`, `producto2_precio`
#   - `producto3_nombre`, `producto3_precio`
#   - (Todos inicializan en `None` o `""`)

# - **Método**: `agregar_producto1(nombre, precio)` que guarde el producto 1

# - **Método**: `agregar_producto2(nombre, precio)` que guarde el producto 2

# - **Método**: `agregar_producto3(nombre, precio)` que guarde el producto 3

# - **Método**: `calcular_total()` que **retorne** la suma de los 3 precios

# - **Método**: `mostrar_productos()` que imprima los 3 productos con sus precios

# - **Prueba**: Agrega 3 productos diferentes y muestra el total

class CarritoCompras:

    # metodo constructor
    def __init__(self):
        self.producto1 = ""
        self.precio1 = 0
        self.producto2 = ""
        self.precio2 = 0
        self.producto3 = ""
        self.precio3 = 0

    # metodos
    def agregar_producto(self, numero, nombre, precio):
        if numero == 1:
            self.producto1 = nombre
            self.precio1 = precio
        elif numero == 2:
            self.producto2 = nombre
            self.precio2 = precio
        elif numero == 3:
            self.producto3 = nombre
            self.precio3 = precio
        else:
            print("Error: Solo se pueden agregar 3 productos")
    
    def calcular_total(self):
        return self.precio1+self.precio2+self.precio3
    
    def mostrar_productos(self):
        print(f"\n--- PRODUCTOS EN CARRITO ---")
        print(f"1. {self.producto1}: ${self.precio1}")
        print(f"2. {self.producto2}: ${self.precio2}")
        print(f"3. {self.producto3}: ${self.precio3}")
        print("---------------------------\n")


print("Sistema de Ventas")
producto = CarritoCompras()
producto.agregar_producto(1, "Huevos", 2455)
producto.agregar_producto(2, "Harina pan", 2355)
producto.agregar_producto(3, "Arroz", 3500)
suma_precios = producto.calcular_total()
print(f"Suma Precios: {suma_precios}")
producto.mostrar_productos()



        


    