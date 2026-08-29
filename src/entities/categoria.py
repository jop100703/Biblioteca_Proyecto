def nueva_categoria(id_categoria, nombre, descripcion):
    """Arma y devuelve una categoría (un diccionario)."""
    return {
        "id_categoria": id_categoria,
        "nombre": nombre,
        "descripcion": descripcion,
    }


def mostrar_categoria(categoria):
    """Texto legible para imprimir una categoría en pantalla."""
    return (
        f"Categoria(id={categoria['id_categoria']}, "
        f"nombre='{categoria['nombre']}', "
        f"descripcion='{categoria['descripcion']}')"
    )
