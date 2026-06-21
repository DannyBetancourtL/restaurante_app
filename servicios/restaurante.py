# Clase encargada de administrar productos y clientes

class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []
        self.clientes = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def mostrar_productos(self):
        print("\n=== PRODUCTOS DISPONIBLES ===")
        for i, producto in enumerate(self.productos, start=1):
            print(f"{i}. {producto}")

    def mostrar_clientes(self):
        print("\n=== CLIENTES REGISTRADOS ===")
        for i, cliente in enumerate(self.clientes, start=1):
            print(f"{i}. {cliente}")

    # Método para registrar una orden
    def tomar_orden(self):
        print("\n========== NUEVA ORDEN ==========")

        self.mostrar_clientes()

        opcion_cliente = int(input("\nSeleccione el número del cliente: "))
        cliente = self.clientes[opcion_cliente - 1]

        pedido = []
        total = 0

        while True:
            self.mostrar_productos()

            opcion = int(input("\nSeleccione el número del producto: "))
            producto = self.productos[opcion - 1]

            pedido.append(producto)
            total += producto.precio

            continuar = input("¿Desea agregar otro producto? (s/n): ")

            if continuar.lower() != "s":
                break

        print("\n========= RESUMEN DEL PEDIDO =========")
        print(f"Cliente: {cliente.nombre}")

        for producto in pedido:
            print(f"- {producto.nombre} : ${producto.precio:.2f}")

        print(f"\nTOTAL A PAGAR: ${total:.2f}")