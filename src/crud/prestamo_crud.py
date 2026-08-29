from src.entities.prestamo import nuevo_prestamo

lista_prestamos = []
siguiente_id = 1


def crear_prestamo(id_usuario, id_ejemplar, fecha_prestamo):
    """CREATE: registra que un usuario se llevó un ejemplar."""
    global siguiente_id

    prestamo = nuevo_prestamo(siguiente_id, id_usuario, id_ejemplar, fecha_prestamo)
    lista_prestamos.append(prestamo)
    siguiente_id = siguiente_id + 1

    return prestamo


def obtener_prestamos():
    """READ: devuelve todos los préstamos."""
    return lista_prestamos


def buscar_prestamo_por_id(id_prestamo):
    """READ: busca un préstamo por su id."""
    for prestamo in lista_prestamos:
        if prestamo["id_prestamo"] == id_prestamo:
            return prestamo
    return None


def actualizar_prestamo(id_prestamo, fecha_devolucion=None, estado=None):
    """UPDATE: por ejemplo, registrar la fecha en que el usuario
    devolvió el libro."""
    prestamo = buscar_prestamo_por_id(id_prestamo)

    if prestamo is None:
        return None

    if fecha_devolucion is not None:
        prestamo["fecha_devolucion"] = fecha_devolucion

    if estado is not None:
        prestamo["estado"] = estado

    return prestamo


def eliminar_prestamo(id_prestamo):
    """DELETE: borra un préstamo de la lista."""
    prestamo = buscar_prestamo_por_id(id_prestamo)

    if prestamo is None:
        return False

    lista_prestamos.remove(prestamo)
    return True
