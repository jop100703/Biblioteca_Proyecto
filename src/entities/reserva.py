def nueva_reserva(id_reserva, id_usuario, id_libro, fecha_reserva, estado="pendiente"):
    #Arma y devuelve una reserva (un diccionario).
    return {
        "id_reserva": id_reserva,
        "id_usuario": id_usuario,  # quién reservó
        "id_libro": id_libro,      # qué libro reservó
        "fecha_reserva": fecha_reserva,
        "estado": estado,  # pendiente / confirmada / cancelada
    }


def mostrar_reserva(reserva):
    #Texto legible para imprimir una reserva en pantalla.
    return (
        f"Reserva(id={reserva['id_reserva']}, "
        f"id_usuario={reserva['id_usuario']}, "
        f"id_libro={reserva['id_libro']}, "
        f"fecha_reserva='{reserva['fecha_reserva']}', "
        f"estado='{reserva['estado']}')"
    )
