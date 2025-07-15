# Módulo para gestionar la base de datos SQLite
import sqlite3

ARCHIVO_BD = "inventario.db"

def conexion_base_datos():
    conexion = sqlite3.connect(ARCHIVO_BD)
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL,
            categoria TEXT
        )
    """)
    conexion.commit()
    conexion.close()
    print("Base de datos conectada y tabla creada.")

def agregar_producto_db(nombre, descripcion, cantidad, precio, categoria):
    conexion = sqlite3.connect(ARCHIVO_BD)
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria) VALUES (?, ?, ?, ?, ?)",
                   (nombre, descripcion, cantidad, precio, categoria))
    conexion.commit()
    conexion.close()

def obtener_productos():
    conexion = sqlite3.connect(ARCHIVO_BD)
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    datos = cursor.fetchall()
    conexion.close()
    return datos

def buscar_producto_por_id(producto_id):
    conexion = sqlite3.connect(ARCHIVO_BD)
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE id = ?", (producto_id,))
    resultado = cursor.fetchone()
    conexion.close()
    return resultado

def eliminar_producto_por_id(producto_id):
    conexion = sqlite3.connect(ARCHIVO_BD)
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM productos WHERE id = ?", (producto_id,))
    conexion.commit()
    conexion.close()

def reporte_stock_bajo(limite):
    conexion = sqlite3.connect(ARCHIVO_BD)
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (limite,))
    datos = cursor.fetchall()
    conexion.close()
    return datos


# Creo base de datos para registrar usuarios 
def conexion_usuarios():
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL UNIQUE,
        clave TEXT NOT NULL
    )
    """)
    conexion.commit()
    conexion.close()

def registrar_usuario(nombre, clave):
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()
    try:
        cursor.execute("INSERT INTO usuarios (nombre, clave) VALUES (?, ?)", (nombre, clave))
        conexion.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conexion.close()

def validar_usuario(nombre, clave):
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE nombre = ? AND clave = ?", (nombre, clave))
    resultado = cursor.fetchone()
    conexion.close()
    return resultado is not None