def nueva_editorial(id_editorial, nombre, pais):
    """Arma y devuelve una editorial (un diccionario)."""
    return {
        "id_editorial": id_editorial,
        "nombre": nombre,
        "pais": pais,
    }


def mostrar_editorial(editorial):
    """Texto legible para imprimir una editorial en pantalla."""
    return (
        f"Editorial(id={editorial['id_editorial']}, "
        f"nombre='{editorial['nombre']}', pais='{editorial['pais']}')"
    )
