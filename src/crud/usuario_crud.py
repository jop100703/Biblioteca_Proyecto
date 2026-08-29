import uuid

from src.entities.usuario import nuevo_usuario

lista_usuarios = []


def crear_usuario(nombre, correo, tipo="estudiante"):
    """CREATE: registra un usuario nuevo."""
    id_usuario = str(uuid.uuid4())
    usuario = nuevo_usuario(id_usuario, nombre, correo, tipo)
    lista_usuarios.append(usuario)

    return usuario


def obtener_usuarios():
    """READ: devuelve todos los usuarios."""
    return lista_usuarios


def buscar_usuario_por_id(id_usuario):
    """READ: busca un usuario por su id."""
    for usuario in lista_usuarios:
        if usuario["id_usuario"] == id_usuario:
            return usuario
    return None


def actualizar_usuario(id_usuario, nombre=None, correo=None):
    """UPDATE: cambia los datos de un usuario existente."""
    usuario = buscar_usuario_por_id(id_usuario)

    if usuario is None:
        return None

    if nombre is not None:
        usuario["nombre"] = nombre

    if correo is not None:
        usuario["correo"] = correo

    return usuario


def eliminar_usuario(id_usuario):
    """DELETE: borra un usuario de la lista."""
    usuario = buscar_usuario_por_id(id_usuario)

    if usuario is None:
        return False

    lista_usuarios.remove(usuario)
    return True
