# Clase hija que representa un platillo.

from modelos.producto import Producto


class Platillo(Producto):

    def __init__(
        self,
        nombre: str,
        precio: float,
        disponible: bool,
        calorias: int
    ):
        super().__init__(nombre, precio, disponible)
        self.calorias = calorias

    def mostrar_informacion(self):
        estado = "Disponible" if self.disponible else "No disponible"

        print(
            f"Platillo: {self.nombre}\n"
            f"Precio: ${self.obtener_precio():.2f}\n"
            f"Calorías: {self.calorias}\n"
            f"Estado: {estado}\n"
        )