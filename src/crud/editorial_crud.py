import uuid

from src.entities.editorial import nueva_editorial

lista_editoriales = []


def crear_editorial(nombre, pais):
    """CREATE: agrega una editorial nueva."""
    id_editorial = str(uuid.uuid4())
    editorial = nueva_editorial(id_editorial, nombre, pais)
    lista_editoriales.append(editorial)

    return editorial


def obtener_editoriales():
    """READ: devuelve todas las editoriales."""
    return lista_editoriales


def buscar_editorial_por_id(id_editorial):
    """READ: busca una editorial por su id."""
    for editorial in lista_editoriales:
        if editorial["id_editorial"] == id_editorial:
            return editorial
    return None


def actualizar_editorial(id_editorial, nombre=None, pais=None):
    """UPDATE: cambia los datos de una editorial existente."""
    editorial = buscar_editorial_por_id(id_editorial)

    if editorial is None:
        return None

    if nombre is not None:
        editorial["nombre"] = nombre

    if pais is not None:
        editorial["pais"] = pais

    return editorial


def eliminar_editorial(id_editorial):
    """DELETE: borra una editorial de la lista."""
    editorial = buscar_editorial_por_id(id_editorial)

    if editorial is None:
        return False

    lista_editoriales.remove(editorial)
    return True
