from src.crud import autor_crud  
from src.crud import editorial_crud
from src.crud import categoria_crud
from src.crud import libro_crud
from src.crud import ejemplar_crud
from src.crud import usuario_crud
from src.crud import prestamo_crud
from src.crud import reserva_crud

from src.entities.autor import mostrar_autor
from src.entities.editorial import mostrar_editorial
from src.entities.categoria import mostrar_categoria
from src.entities.libro import mostrar_libro
from src.entities.ejemplar import mostrar_ejemplar
from src.entities.usuario import mostrar_usuario
from src.entities.prestamo import mostrar_prestamo
from src.entities.reserva import mostrar_reserva


def titulo(texto):
    print()
    print("=" * 60)
    print(texto)
    print("=" * 60)


# ---------------------------------------------------------------
# 1. CREAR REGISTROS (Create)
# ---------------------------------------------------------------
titulo("1. CREACIÓN DE REGISTROS")

autor1 = autor_crud.crear_autor("Gabriel García Márquez", "Colombiana")
autor2 = autor_crud.crear_autor("Jorge Luis Borges", "Argentina")
print("Autores creados:")
print(" -", mostrar_autor(autor1))
print(" -", mostrar_autor(autor2))

editorial1 = editorial_crud.crear_editorial("Editorial Sudamericana", "Argentina")
print("\nEditorial creada:")
print(" -", mostrar_editorial(editorial1))

categoria1 = categoria_crud.crear_categoria(
    "Realismo mágico", "Narrativa con elementos fantásticos"
)
print("\nCategoría creada:")
print(" -", mostrar_categoria(categoria1))
 
libro1 = libro_crud.crear_libro(
    "Cien años de soledad",
    autor1["id_autor"],
    editorial1["id_editorial"],
    categoria1["id_categoria"],
    1967,
)
print("\nLibro creado:")
print(" -", mostrar_libro(libro1))

ejemplar1 = ejemplar_crud.crear_ejemplar(libro1["id_libro"], "INV-001")
ejemplar2 = ejemplar_crud.crear_ejemplar(libro1["id_libro"], "INV-002")
print("\nEjemplares creados:")
print(" -", mostrar_ejemplar(ejemplar1))
print(" -", mostrar_ejemplar(ejemplar2))

usuario1 = usuario_crud.crear_usuario(
    "Juan Pérez", "juan.perez@correo.edu", "estudiante"
)
usuario2 = usuario_crud.crear_usuario(
    "María Gómez", "maria.gomez@correo.edu", "profesor"
)
print("\nUsuarios creados:")
print(" -", mostrar_usuario(usuario1))
print(" -", mostrar_usuario(usuario2))

prestamo1 = prestamo_crud.crear_prestamo(
    usuario1["id_usuario"], ejemplar1["id_ejemplar"], "2026-08-20"
)
print("\nPréstamo creado:")
print(" -", mostrar_prestamo(prestamo1))

reserva1 = reserva_crud.crear_reserva(
    usuario2["id_usuario"], libro1["id_libro"], "2026-08-21"
)
print("\nReserva creada:")
print(" -", mostrar_reserva(reserva1))


# ---------------------------------------------------------------
# 2. CONSULTAR REGISTROS (Read)
# ---------------------------------------------------------------
titulo("2. CONSULTA DE REGISTROS")

print("Autores:")
for autor in autor_crud.obtener_autores():
    print(" -", mostrar_autor(autor))

print("\nEditoriales:")
for editorial in editorial_crud.obtener_editoriales():
    print(" -", mostrar_editorial(editorial))

print("\nCategorías:")
for categoria in categoria_crud.obtener_categorias():
    print(" -", mostrar_categoria(categoria))

print("\nLibros:")
for libro in libro_crud.obtener_libros():
    print(" -", mostrar_libro(libro))

print("\nEjemplares:")
for ejemplar in ejemplar_crud.obtener_ejemplares():
    print(" -", mostrar_ejemplar(ejemplar))

print("\nUsuarios:")
for usuario in usuario_crud.obtener_usuarios():
    print(" -", mostrar_usuario(usuario))

print("\nPréstamos:")
for prestamo in prestamo_crud.obtener_prestamos():
    print(" -", mostrar_prestamo(prestamo))

print("\nReservas:")
for reserva in reserva_crud.obtener_reservas():
    print(" -", mostrar_reserva(reserva))


# ---------------------------------------------------------------
# 3. VER CÓMO SE RELACIONAN LAS ENTIDADES
# ---------------------------------------------------------------
titulo("3. RELACIÓN ENTRE ENTIDADES")

autor_del_libro = autor_crud.buscar_autor_por_id(libro1["id_autor"])
editorial_del_libro = editorial_crud.buscar_editorial_por_id(libro1["id_editorial"])
categoria_del_libro = categoria_crud.buscar_categoria_por_id(libro1["id_categoria"])

print(
    f"El libro '{libro1['titulo']}' fue escrito por "
    f"{autor_del_libro['nombre']}, publicado por "
    f"{editorial_del_libro['nombre']}, y es de la categoría "
    f"'{categoria_del_libro['nombre']}'."
)

usuario_del_prestamo = usuario_crud.buscar_usuario_por_id(prestamo1["id_usuario"])
ejemplar_prestado = ejemplar_crud.buscar_ejemplar_por_id(prestamo1["id_ejemplar"])
libro_prestado = libro_crud.buscar_libro_por_id(ejemplar_prestado["id_libro"])

print(
    f"{usuario_del_prestamo['nombre']} tiene prestado el ejemplar "
    f"'{ejemplar_prestado['codigo_inventario']}' del libro "
    f"'{libro_prestado['titulo']}'."
)

# Y para la reserva.
usuario_de_reserva = usuario_crud.buscar_usuario_por_id(reserva1["id_usuario"])
libro_reservado = libro_crud.buscar_libro_por_id(reserva1["id_libro"])

print(
    f"{usuario_de_reserva['nombre']} reservó el libro "
    f"'{libro_reservado['titulo']}'."
)


# ---------------------------------------------------------------
# 4. ACTUALIZAR REGISTROS (Update)
# ---------------------------------------------------------------
titulo("4. ACTUALIZACIÓN DE REGISTROS")

autor_crud.actualizar_autor(autor1["id_autor"], nacionalidad="Colombia")
print("Autor actualizado:")
print(" -", mostrar_autor(autor_crud.buscar_autor_por_id(autor1["id_autor"])))

ejemplar_crud.actualizar_ejemplar(ejemplar1["id_ejemplar"], estado="prestado")
print("\nEjemplar actualizado:")
print(" -", mostrar_ejemplar(ejemplar_crud.buscar_ejemplar_por_id(ejemplar1["id_ejemplar"])))

prestamo_crud.actualizar_prestamo(
    prestamo1["id_prestamo"],
    fecha_devolucion="2026-09-05",
    estado="devuelto",
)
print("\nPréstamo actualizado:")
print(" -", mostrar_prestamo(prestamo_crud.buscar_prestamo_por_id(prestamo1["id_prestamo"])))

reserva_crud.actualizar_reserva(reserva1["id_reserva"], estado="confirmada")
print("\nReserva actualizada:")
print(" -", mostrar_reserva(reserva_crud.buscar_reserva_por_id(reserva1["id_reserva"])))


# ---------------------------------------------------------------
# 5. ELIMINAR UN REGISTRO (Delete)
# ---------------------------------------------------------------
titulo("5. ELIMINACIÓN DE REGISTROS")

se_elimino = ejemplar_crud.eliminar_ejemplar(ejemplar2["id_ejemplar"])
print(f"¿Se eliminó el ejemplar 2? {se_elimino}")

print("\nEjemplares que quedan:")
for ejemplar in ejemplar_crud.obtener_ejemplares():
    print(" -", mostrar_ejemplar(ejemplar))


titulo("FIN DE LA DEMOSTRACIÓN")
