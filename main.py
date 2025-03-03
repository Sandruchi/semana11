# main.py
from Inventario import Inventario
from Producto import Producto


def menu():
    inventario = Inventario()
    archivo = "inventario.json"

    # Cargar inventario desde archivo
    inventario.cargar_inventario(archivo)

    while True:
        print("\n--- Sistema de Gestión de Inventario ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            # Añadir un nuevo producto
            producto_id = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad del producto: "))
            precio = float(input("Precio del producto: "))
            producto = Producto(producto_id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == '2':
            # Eliminar producto
            producto_id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(producto_id)

        elif opcion == '3':
            # Actualizar producto
            producto_id = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (deja vacío para no cambiar): ")
            precio = input("Nuevo precio (deja vacío para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(producto_id, cantidad, precio)

        elif opcion == '4':
            # Buscar producto
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == '5':
            # Mostrar todos los productos
            inventario.mostrar_inventario()

        elif opcion == '6':
            # Guardar inventario
            inventario.guardar_inventario(archivo)

        elif opcion == '7':
            # Salir
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor intente de nuevo.")


if __name__ == "__main__":
    menu()