import uuid

from src.entities.reserva import nueva_reserva

lista_reservas = []


def crear_reserva(id_usuario, id_libro, fecha_reserva):
    """CREATE: registra que un usuario reservó un libro."""
    id_reserva = str(uuid.uuid4())
    reserva = nueva_reserva(id_reserva, id_usuario, id_libro, fecha_reserva)
    lista_reservas.append(reserva)

    return reserva


def obtener_reservas():
    """READ: devuelve todas las reservas."""
    return lista_reservas


def buscar_reserva_por_id(id_reserva):
    """READ: busca una reserva por su id."""
    for reserva in lista_reservas:
        if reserva["id_reserva"] == id_reserva:
            return reserva
    return None


def actualizar_reserva(id_reserva, estado=None):
    """UPDATE: cambia el estado de una reserva (por ejemplo, de
    'pendiente' a 'confirmada')."""
    reserva = buscar_reserva_por_id(id_reserva)

    if reserva is None:
        return None

    if estado is not None:
        reserva["estado"] = estado

    return reserva


def eliminar_reserva(id_reserva):
    """DELETE: borra una reserva de la lista."""
    reserva = buscar_reserva_por_id(id_reserva)

    if reserva is None:
        return False

    lista_reservas.remove(reserva)
    return True
