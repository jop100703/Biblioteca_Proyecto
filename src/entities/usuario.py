def nuevo_usuario(id_usuario, nombre, correo, tipo="estudiante"):
    """Arma y devuelve un usuario (un diccionario)."""
    return {
        "id_usuario": id_usuario,
        "nombre": nombre,
        "correo": correo,
        "tipo": tipo,  # "estudiante" o "profesor"
    }


def mostrar_usuario(usuario):
    """Texto legible para imprimir un usuario en pantalla."""
    return (
        f"Usuario(id={usuario['id_usuario']}, nombre='{usuario['nombre']}', "
        f"correo='{usuario['correo']}', tipo='{usuario['tipo']}')"
    )
