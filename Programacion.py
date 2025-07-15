# Módulo de funciones del programa
import os
import BaseDatos
import Interfas

def elegir_menu():
    return input("\n> ")

def agregar_producto():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== Agregar Producto ===")
    nombre = input("Nombre: ").strip().capitalize()
    descripcion = input("Descripción: ").strip()
    
    while True:
        try:
            cantidad = int(input("Cantidad: "))
            break
        except ValueError:
            print("Ingrese un número entero para la cantidad.")

    while True:
        try:
            precio = float(input("Precio: "))
            break
        except ValueError:
            print("Ingrese un número válido para el precio.")

    categoria = input("Categoría: ").strip().capitalize()
    
    BaseDatos.agregar_producto_db(nombre, descripcion, cantidad, precio, categoria)
    print(f"Producto '{nombre}' agregado exitosamente.")
    input("Presione Enter para continuar...")

def mostrar_productos():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== Lista de Productos ===")
    productos = BaseDatos.obtener_productos()
    if not productos:
        print("No hay productos cargados.")
    else:
        for prod in productos:
            print(f"{prod[0]}. {prod[1]} ({prod[2]}) - Cantidad: {prod[3]}, Precio: ${prod[4]}, Categoría: {prod[5]}")
    input("Presione Enter para continuar...")

def buscar_producto():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== Buscar Producto por ID ===")
    try:
        producto_id = int(input("Ingrese el ID del producto: "))
        producto = BaseDatos.buscar_producto_por_id(producto_id)
        if producto:
            print(f"\nID: {producto[0]}\nNombre: {producto[1]}\nDescripción: {producto[2]}\nCantidad: {producto[3]}\nPrecio: ${producto[4]}\nCategoría: {producto[5]}")
        else:
            print("Producto no encontrado.")
    except ValueError:
        print("ID inválido.")
    input("Presione Enter para continuar...")

def eliminar_producto():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== Eliminar Producto por ID ===")
    try:
        producto_id = int(input("Ingrese el ID del producto a eliminar: "))
        BaseDatos.eliminar_producto_por_id(producto_id)
        print("Producto eliminado.")
    except ValueError:
        print("ID inválido.")
    input("Presione Enter para continuar...")

def reporte_stock():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== Reporte de Stock Bajo ===")
    try:
        limite = int(input("Mostrar productos con cantidad menor o igual a: "))
        productos = BaseDatos.reporte_stock_bajo(limite)
        if productos:
            for p in productos:
                print(f"{p[0]}. {p[1]} - Cantidad: {p[3]}")
        else:
            print("No hay productos con esa condición.")
    except ValueError:
        print("Cantidad inválida.")
    input("Presione Enter para continuar...")

def cerrando_programa():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Gracias por usar el sistema de inventario.")
    exit()

def iniciar_sesion():
    while True:
        opcion = input().strip().lower()
        if opcion == "s":
            nombre = input("Nombre de usuario: ").strip()
            clave = input("Contraseña: ").strip()
            if BaseDatos.validar_usuario(nombre, clave):
                print(f"Bienvenido {nombre}!")
                return nombre
            else:
                print("Usuario o contraseña incorrectos.")
        elif opcion == "r":
            nombre = input("Elija un nombre de usuario: ").strip()
            clave = input("Elija una contraseña: ").strip()
            if BaseDatos.registrar_usuario(nombre, clave):
                print("Registro exitoso. Ahora puede iniciar sesión.")
            else:
                print("El usuario ya existe. Intente otro.")
        elif opcion == "x":
            print("Saliendo del programa.")
            exit()
        else:
            print("Opción inválida.")
