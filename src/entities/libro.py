def nuevo_libro(
    id_libro, titulo, id_autor, id_editorial, id_categoria, anio_publicacion
):
    """Arma y devuelve un libro (un diccionario) conectado con un
    autor, una editorial y una categoría a través de sus id."""
    return {
        "id_libro": id_libro,
        "titulo": titulo,
        "id_autor": id_autor,          # a qué autor pertenece
        "id_editorial": id_editorial,  # qué editorial lo publicó
        "id_categoria": id_categoria,  # a qué categoría pertenece
        "anio_publicacion": anio_publicacion,
    }


def mostrar_libro(libro):
    """Texto legible para imprimir un libro en pantalla."""
    return (
        f"Libro(id={libro['id_libro']}, titulo='{libro['titulo']}', "
        f"id_autor={libro['id_autor']}, id_editorial={libro['id_editorial']}, "
        f"id_categoria={libro['id_categoria']}, "
        f"anio_publicacion={libro['anio_publicacion']})"
    )
