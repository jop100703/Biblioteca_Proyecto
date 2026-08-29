def nuevo_prestamo(
    id_prestamo,
    id_usuario,
    id_ejemplar,
    fecha_prestamo,
    fecha_devolucion=None,
    estado="activo",
):
    """Arma y devuelve un préstamo (un diccionario)."""
    return {
        "id_prestamo": id_prestamo,
        "id_usuario": id_usuario,    # quién pidió el préstamo
        "id_ejemplar": id_ejemplar,  # qué copia se llevó
        "fecha_prestamo": fecha_prestamo,
        "fecha_devolucion": fecha_devolucion,  # aún no se sabe, por eso None
        "estado": estado,  # activo / pendiente_devolucion / devuelto
    }


def mostrar_prestamo(prestamo):
    """Texto legible para imprimir un préstamo en pantalla."""
    return (
        f"Prestamo(id={prestamo['id_prestamo']}, "
        f"id_usuario={prestamo['id_usuario']}, "
        f"id_ejemplar={prestamo['id_ejemplar']}, "
        f"fecha_prestamo='{prestamo['fecha_prestamo']}', "
        f"fecha_devolucion={prestamo['fecha_devolucion']!r}, "
        f"estado='{prestamo['estado']}')"
    )
