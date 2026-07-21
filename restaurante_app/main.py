# Punto de inicio del programa.

from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante


restaurante = Restaurante("Sabores del Pacífico")


platillo1 = Platillo(
    "Arroz Marinero",
    8.50,
    True,
    650
)

platillo2 = Platillo(
    "Seco de Pollo",
    7.25,
    True,
    580
)


bebida1 = Bebida(
    "Limonada",
    2.50,
    True,
    500
)

bebida2 = Bebida(
    "Jugo de Mora",
    3.00,
    True,
    400
)


restaurante.agregar_producto(platillo1)
restaurante.agregar_producto(platillo2)
restaurante.agregar_producto(bebida1)
restaurante.agregar_producto(bebida2)


restaurante.mostrar_productos()