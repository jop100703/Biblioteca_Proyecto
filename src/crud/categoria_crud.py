import uuid

from src.entities.categoria import nueva_categoria

lista_categorias = []


def crear_categoria(nombre, descripcion):
    """CREATE: agrega una categoría nueva."""
    id_categoria = str(uuid.uuid4())
    categoria = nueva_categoria(id_categoria, nombre, descripcion)
    lista_categorias.append(categoria)

    return categoria


def obtener_categorias():
    """READ: devuelve todas las categorías."""
    return lista_categorias


def buscar_categoria_por_id(id_categoria):
    """READ: busca una categoría por su id."""
    for categoria in lista_categorias:
        if categoria["id_categoria"] == id_categoria:
            return categoria
    return None


def actualizar_categoria(id_categoria, nombre=None, descripcion=None):
    """UPDATE: cambia los datos de una categoría existente."""
    categoria = buscar_categoria_por_id(id_categoria)

    if categoria is None:
        return None

    if nombre is not None:
        categoria["nombre"] = nombre

    if descripcion is not None:
        categoria["descripcion"] = descripcion

    return categoria


def eliminar_categoria(id_categoria):
    """DELETE: borra una categoría de la lista."""
    categoria = buscar_categoria_por_id(id_categoria)

    if categoria is None:
        return False

    lista_categorias.remove(categoria)
    return True
