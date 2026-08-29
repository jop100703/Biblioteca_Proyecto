def nuevo_autor(id_autor, nombre, nacionalidad):
    return {
        "id_autor": id_autor,
        "nombre": nombre,
        "nacionalidad": nacionalidad,
    }


def mostrar_autor(autor):
    return (
        f"Autor(id={autor['id_autor']}, nombre='{autor['nombre']}', "
        f"nacionalidad='{autor['nacionalidad']}')"
    )
