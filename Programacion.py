# Módulo de funciones del programa
import os
import BaseDatos
import Interfas

def elegir_menu():
    return input("\n> ")

def agregar_producto():
    Interfas.limpiar_pantalla()
    Interfas.estilo("Agregar Producto")
    Interfas.estilo("Nombre:")
    nombre = input().strip().capitalize()
    Interfas.estilo("Descripción:")
    descripcion = input("").strip()
    
    while True:
        try:
            Interfas.estilo("Cantidad:")
            cantidad = int(input())
            break
        except ValueError:
            Interfas.estilo("Ingrese un numero para la cantidad.")
            print()

    while True:
        try:
            precio = float(input("Precio: "))
            break
        except ValueError:
            Interfas.estilo("Ingrese un número válido para el precio.")
            print()
    Interfas.estilo("Categoria:")
    categoria = input().strip().capitalize()
    
    BaseDatos.agregar_producto_db(nombre, descripcion, cantidad, precio, categoria)
    Interfas.estilo(f"Producto '{nombre}' agregado exitosamente.")
    Interfas.estilo("Presione Enter para continuar...")

def mostrar_productos():
    Interfas.limpiar_pantalla()
    Interfas.estilo("Lista de Productos")
    productos = BaseDatos.obtener_productos()
    if not productos:
        Interfas.estilo("No hay productos cargados.")
    else:
        for prod in productos:
            Interfas.estilo(f"{prod[0]}. {prod[1]} ({prod[2]}) - Cantidad: {prod[3]}, Precio: ${prod[4]}, Categoría: {prod[5]}")
    Interfas.estilo("Presione Enter para continuar...")
    input()

def buscar_producto():
    Interfas.limpiar_pantalla()
    Interfas.estilo("Buscar Producto por ID")
    try:
        Interfas.estilo("Ingrese el ID del producto:")
        producto_id = int(input())
        producto = BaseDatos.buscar_producto_por_id(producto_id)
        if producto:
            Interfas.estilo(f"\nID: {producto[0]}\nNombre: {producto[1]}\nDescripción: {producto[2]}\nCantidad: {producto[3]}\nPrecio: ${producto[4]}\nCategoría: {producto[5]}")
        else:
            Interfas.estilo("Producto no encontrado.")
    except ValueError:
        Interfas.estilo("ID inválido.")
        Interfas.estilo("Presione Enter para continuar...")
    input()

def eliminar_producto():
    Interfas.limpiar_pantalla()
    Interfas.estilo("Eliminar Producto por ID")
    try:
        Interfas.estilo("Ingrese el ID del producto a eliminar: ")
        producto_id = int(input())
        BaseDatos.eliminar_producto_por_id(producto_id)
        Interfas.estilo("Producto eliminado.")
    except ValueError:
        Interfas.estilo("ID inválido.")
        Interfas.estilo("Presione Enter para continuar...")
    input()

def reporte_stock():
    Interfas.limpiar_pantalla()
    Interfas.estilo("Reporte de Stock Bajo")
    try:
        Interfas.estilo("Mostrar productos con cantidad menor o igual a: ")
        limite = int(input())
        productos = BaseDatos.reporte_stock_bajo(limite)
        if productos:
            for p in productos:
                Interfas.estilo(f"{p[0]}. {p[1]} - Cantidad: {p[3]}")
        else:
            Interfas.estilo("No hay productos con esa condición.")
    except ValueError:
        Interfas.estilo("Cantidad inválida.")
        Interfas.estilo("Presione Enter para continuar...")
    input()

def cerrando_programa():
    Interfas.limpiar_pantalla()
    Interfas.estilo("Gracias por usar el sistema de inventario.")
    exit()

def iniciar_sesion():
    while True:
        opcion = input().strip().lower()
        if opcion == "i":
            Interfas.limpiar_pantalla()
            Interfas.estilo("Nombre de usuario:")
            nombre = input("> ").strip()
            Interfas.estilo("Contraseña:")
            clave = input("> ").strip()
            
            if BaseDatos.validar_usuario(nombre, clave):
                Interfas.limpiar_pantalla()
                Interfas.estilo(f"Bienvenido {nombre}!")
                Interfas.estilo("Ingrese enter para continuar")
                input("")
                return 
            
            else:
                Interfas.limpiar_pantalla()
                Interfas.estilo("Usuario o contraseña incorrectos.")
                Interfas.iniciar_sesion()
                input()
                

        elif opcion == "r":
            Interfas.estilo("Elija un nombre de usuario: ")
            nombre = input("> ").strip()
            Interfas.estilo("Elija una contraseña: ")
            clave = input("> ").strip()
            if BaseDatos.registrar_usuario(nombre, clave):
                Interfas.limpiar_pantalla()
                Interfas.estilo("Registro exitoso. Ahora puede iniciar sesión.")
                Interfas.iniciar_sesion()
                continue
            else:
                Interfas.estilo("El usuario ya existe. Intente otro.")
        elif opcion == "x":
            Interfas.limpiar_pantalla()
            Interfas.estilo("Saliendo del programa.")
            Interfas.estilo("Muchas gracias por usar el programa creado por BONZI CEFERINO JOSÉ")
            exit()
        else:
            Interfas.limpiar_pantalla()
            Interfas.estilo("Opción inválida.")
            Interfas.iniciar_sesion()

