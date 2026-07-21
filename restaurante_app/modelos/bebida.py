# Clase hija que representa una bebida.

from modelos.producto import Producto


class Bebida(Producto):

    def __init__(
        self,
        nombre: str,
        precio: float,
        disponible: bool,
        volumen_ml: int
    ):
        super().__init__(nombre, precio, disponible)
        self.volumen_ml = volumen_ml

    def mostrar_informacion(self):
        estado = "Disponible" if self.disponible else "No disponible"

        print(
            f"Bebida: {self.nombre}\n"
            f"Precio: ${self.obtener_precio():.2f}\n"
            f"Volumen: {self.volumen_ml} ml\n"
            f"Estado: {estado}\n"
        )