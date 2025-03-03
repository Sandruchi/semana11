# Inventario.py
from Producto import Producto
import json

class Inventario:
    def __init__(self):
        self.inventario = {}

    def añadir_producto(self, producto):
        if producto.obtener_id() not in self.inventario:
            self.inventario[producto.obtener_id()] = producto
            print(f"Producto '{producto.obtener_nombre()}' añadido al inventario.")
        else:
            print("Error: Ya existe un producto con ese ID.")

    def eliminar_producto(self, producto_id):
        if producto_id in self.inventario:
            producto = self.inventario.pop(producto_id)
            print(f"Producto '{producto.obtener_nombre()}' eliminado.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, producto_id, cantidad=None, precio=None):
        if producto_id in self.inventario:
            producto = self.inventario[producto_id]
            if cantidad is not None:
                producto.establecer_cantidad(cantidad)
            if precio is not None:
                producto.establecer_precio(precio)
            print(f"Producto '{producto.obtener_nombre()}' actualizado.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        encontrados = [producto for producto in self.inventario.values() if nombre.lower() in producto.obtener_nombre().lower()]
        if encontrados:
            for producto in encontrados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_inventario(self):
        if self.inventario:
            for producto in self.inventario.values():
                print(producto)
        else:
            print("El inventario está vacío.")

    def guardar_inventario(self, archivo):
        with open(archivo, 'w') as f:
            json.dump({id: vars(producto) for id, producto in self.inventario.items()}, f, indent=4)
        print("Inventario guardado en archivo.")

    def cargar_inventario(self, archivo):
        try:
            with open(archivo, 'r') as f:
                datos = json.load(f)
                for producto_id, producto_data in datos.items():
                    producto = Producto(producto_id, producto_data['nombre'], producto_data['cantidad'], producto_data['precio'])
                    self.inventario[producto_id] = producto
            print("Inventario cargado desde archivo.")
        except FileNotFoundError:
            print("No se encontró el archivo, comenzando con inventario vacío.")