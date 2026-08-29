import uuid

from src.entities.libro import nuevo_libro

lista_libros = []


def crear_libro(
    titulo, id_autor, id_editorial, id_categoria, anio_publicacion
):
    """CREATE: agrega un libro nuevo.
    """
    id_libro = str(uuid.uuid4())

    libro = nuevo_libro(
        id_libro,
        titulo,
        id_autor,
        id_editorial,
        id_categoria,
        anio_publicacion,
    )
    lista_libros.append(libro)

    return libro


def obtener_libros():
    """READ: devuelve todos los libros."""
    return lista_libros


def buscar_libro_por_id(id_libro):
    """READ: busca un libro por su id."""
    for libro in lista_libros:
        if libro["id_libro"] == id_libro:
            return libro
    return None


def actualizar_libro(id_libro, titulo=None, anio_publicacion=None):
    """UPDATE: cambia los datos de un libro existente."""
    libro = buscar_libro_por_id(id_libro)

    if libro is None:
        return None

    if titulo is not None:
        libro["titulo"] = titulo

    if anio_publicacion is not None:
        libro["anio_publicacion"] = anio_publicacion

    return libro


def eliminar_libro(id_libro):
    """DELETE: borra un libro de la lista."""
    libro = buscar_libro_por_id(id_libro)

    if libro is None:
        return False

    lista_libros.remove(libro)
    return True
