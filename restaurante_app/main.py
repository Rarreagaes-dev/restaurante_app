# Punto de inicio del programa.

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


# Crear el restaurante
restaurante = Restaurante("Sabores del Pacífico")


# Crear productos
producto1 = Producto(
    "Arroz Marinero",
    "Plato fuerte",
    8.50,
    True
)

producto2 = Producto(
    "Limonada Natural",
    "Bebida",
    2.25,
    True
)


# Crear clientes
cliente1 = Cliente(
    "María López",
    28,
    "maria@gmail.com",
    True
)

cliente2 = Cliente(
    "Carlos Pérez",
    35,
    "carlos@gmail.com",
    False
)


# Agregar productos al restaurante
restaurante.agregar_producto(producto1)
restaurante.agregar_producto(producto2)


# Agregar clientes al restaurante
restaurante.agregar_cliente(cliente1)
restaurante.agregar_cliente(cliente2)


# Mostrar información
print(restaurante)

restaurante.mostrar_productos()

restaurante.mostrar_clientes()