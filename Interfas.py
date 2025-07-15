# Módulo de interfaz de usuario
import os                                      # Necesario para borrar pantalla y tomar medida del ancho del terminal
from colorama import init, Fore, Back, Style   # Agregar color
init(autoreset=True)                           # Para que los colores se reseteen automáticamente después de cada print  
ancho = os.get_terminal_size().columns         # Grabo en variable el ancho del terminal
fondo = Back.BLUE + Style.BRIGHT + Fore.BLACK

def limpiar_pantalla():                        # Para limpiar la pantalla y mejorar visual
    os.system('cls' if os.name == 'nt' else 'clear')

def centrar_texto(texto, ancho):               # Centrar todo automaticamente
    texto = str(texto)
    espacios_totales = max(ancho - len(texto), 0)
    izquierda = espacios_totales // 2
    derecha = espacios_totales - izquierda
    return (" " * izquierda) + texto + (" " * derecha)


def relleno(color_fondo,ancho):                      # Para rellenar espacios
    print(color_fondo + " " * ancho) 

def estilo(texto):                                    # Estilo a usar 
    relleno(fondo,ancho)
    print(fondo + centrar_texto(texto, ancho))                                                      
    relleno(fondo,ancho)

def mensaje_bienvenida():
    limpiar_pantalla()
    texto = "BIENVENIDO AL SISTEMA DE INVENTARIO"
    estilo(texto) 

def menu_inicio(nombre):
    limpiar_pantalla()
    estilo(f"Progama de Compras Online Bienvenido {nombre}")
    estilo("1. Agregar producto                 2. Mostrar productos")
    estilo("3. Buscar producto                  4. Eliminar producto")
    estilo("5. Stock Minimo                     6. SALIR             ")
    estilo("Ingrese la opción deseada")

def iniciar_sesion():
    texto = "| Iniciar Sesion (I) |  Registrarse  R  |      Salir  X      |"
    estilo(texto)

