# Clase que administra los productos.

from modelos.producto import Producto


class Restaurante:

    def __init__(self, nombre: str):
        self.nombre = nombre
        self.productos: list[Producto] = []

    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)

    def mostrar_productos(self):

        print(f"\n=== {self.nombre} ===\n")

        for producto in self.productos:
            producto.mostrar_informacion()