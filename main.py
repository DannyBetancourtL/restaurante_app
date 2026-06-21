from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

# Crear restaurante
restaurante = Restaurante("***Sabor Lojano ***")

# Crear productos
producto1 = Producto("P001", "Humitas", 1.50, "Plato Principal")
producto2 = Producto("P002", "Cafe filtrado", 1.00, "Bebida")
producto3 = Producto("P003", "Higos con miel", 1.00, "Postre")
producto4 = Producto("P004", "Fritada", 3.50, "Plato Principal")

# Registrar productos
restaurante.agregar_producto(producto1)
restaurante.agregar_producto(producto2)
restaurante.agregar_producto(producto3)
restaurante.agregar_producto(producto4)

# Crear clientes
cliente1 = Cliente("1101234567", "Danny Betancourt", "0987654321")
cliente2 = Cliente("1109876543", "Manuel Torres", "0998765432")

# Registrar clientes
restaurante.agregar_cliente(cliente1)
restaurante.agregar_cliente(cliente2)

# Menú principal
while True:
    print("\n===================================")
    print(" SISTEMA DE GESTIÓN DE RESTAURANTE SABOR LOJANO")
    print("===================================")
    print("1. Ver productos")
    print("2. Ver clientes")
    print("3. Tomar orden")
    print("4. Salir")

    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
        restaurante.mostrar_productos()

    elif opcion == "2":
        restaurante.mostrar_clientes()

    elif opcion == "3":
        restaurante.tomar_orden()

    elif opcion == "4":
        print("\nGracias por utilizar el sistema.")
        break

    else:
        print("\nOpción no válida.")