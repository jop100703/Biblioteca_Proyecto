import uuid

from src.entities.autor import nuevo_autor

# Lista donde se guardan todos los autores creados.
lista_autores = []


def crear_autor(nombre, nacionalidad):
    """CREATE: agrega un autor nuevo a la lista."""
    id_autor = str(uuid.uuid4())  # id único generado automáticamente
    autor = nuevo_autor(id_autor, nombre, nacionalidad)
    lista_autores.append(autor)

    return autor


def obtener_autores():
    """READ: devuelve la lista completa de autores."""
    return lista_autores


def buscar_autor_por_id(id_autor):
    """READ: busca un autor específico por su id. Si no lo
    encuentra, devuelve None (nada)."""
    for autor in lista_autores:
        if autor["id_autor"] == id_autor:
            return autor
    return None


def actualizar_autor(id_autor, nombre=None, nacionalidad=None):
    """UPDATE: cambia los datos de un autor que ya existe.

    Solo se cambian los datos que sí se envían. Si no envías
    'nombre', por ejemplo, el nombre se queda como estaba.
    """
    autor = buscar_autor_por_id(id_autor)

    if autor is None:
        return None  # no existe ese autor, no hay nada que actualizar

    if nombre is not None:
        autor["nombre"] = nombre

    if nacionalidad is not None:
        autor["nacionalidad"] = nacionalidad

    return autor


def eliminar_autor(id_autor):
    """DELETE: borra un autor de la lista. Devuelve True si lo
    borró, False si no lo encontró."""
    autor = buscar_autor_por_id(id_autor)

    if autor is None:
        return False

    lista_autores.remove(autor)
    return True
