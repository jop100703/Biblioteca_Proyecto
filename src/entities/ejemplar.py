def nuevo_ejemplar(
    id_ejemplar, id_libro, codigo_inventario, estado="disponible"
):
    """Arma y devuelve un ejemplar (un diccionario)."""
    return {
        "id_ejemplar": id_ejemplar,
        "id_libro": id_libro,  # a qué libro pertenece esta copia
        # etiqueta física, ej: "INV-001"
        "codigo_inventario": codigo_inventario,
        "estado": estado,  # disponible / prestado / dañado, etc.
    }


def mostrar_ejemplar(ejemplar):
    """Texto legible para imprimir un ejemplar en pantalla."""
    return (
        f"Ejemplar(id={ejemplar['id_ejemplar']}, "
        f"id_libro={ejemplar['id_libro']}, "
        f"codigo_inventario='{ejemplar['codigo_inventario']}', "
        f"estado='{ejemplar['estado']}')"
    )
