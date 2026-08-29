import uuid

from src.entities.ejemplar import nuevo_ejemplar

lista_ejemplares = []


def crear_ejemplar(id_libro, codigo_inventario, estado="disponible"):
    """CREATE: agrega una copia nueva de un libro."""
    id_ejemplar = str(uuid.uuid4())
    ejemplar = nuevo_ejemplar(
        id_ejemplar, id_libro, codigo_inventario, estado
    )
    lista_ejemplares.append(ejemplar)

    return ejemplar


def obtener_ejemplares():
    """READ: devuelve todos los ejemplares."""
    return lista_ejemplares


def buscar_ejemplar_por_id(id_ejemplar):
    """READ: busca un ejemplar por su id."""
    for ejemplar in lista_ejemplares:
        if ejemplar["id_ejemplar"] == id_ejemplar:
            return ejemplar
    return None


def actualizar_ejemplar(id_ejemplar, estado=None):
    """UPDATE: cambia el estado de un ejemplar (por ejemplo, de
    'disponible' a 'prestado')."""
    ejemplar = buscar_ejemplar_por_id(id_ejemplar)

    if ejemplar is None:
        return None

    if estado is not None:
        ejemplar["estado"] = estado

    return ejemplar


def eliminar_ejemplar(id_ejemplar):
    """DELETE: borra un ejemplar de la lista."""
    ejemplar = buscar_ejemplar_por_id(id_ejemplar)

    if ejemplar is None:
        return False

    lista_ejemplares.remove(ejemplar)
    return True
