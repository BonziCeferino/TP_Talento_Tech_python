# Módulo de interfaz de usuario
import os                                      # Necesario para borrar pantalla y tomar medida del ancho del terminal
from colorama import init, Fore, Back, Style   # Agregar color
init(autoreset=True)                           # Para que los colores se reseteen automáticamente después de cada print  
ancho = os.get_terminal_size().columns         # Grabo en variable el ancho del terminal
fondo = Back.BLUE + Style.BRIGHT + Fore.BLACK

def centrar_texto(texto, ancho):
    texto = str(texto)
    espacios_totales = max(ancho - len(texto), 0)
    izquierda = espacios_totales // 2
    derecha = espacios_totales - izquierda
    return (" " * izquierda) + texto + (" " * derecha)


def relleno(color_fondo,ancho):                      # Para rellenar espacios
    print(color_fondo + " " * ancho) 

def mensaje_bienvenida():
    os.system('cls' if os.name == 'nt' else 'clear')
    texto = "BIENVENIDO AL SISTEMA DE INVENTARIO"
    relleno(fondo,ancho)
    relleno(fondo,ancho)
    print(fondo + centrar_texto(texto, ancho))                                                      
    relleno(fondo,ancho)
    relleno(fondo,ancho) 

def menu_inicio(nombre):
    os.system('cls')
    print("\n")
    print("************************************************************")
    print("+++++++++++++++  Programa de compras Online ++++++++++++++++")
    print("************************************************************\n")
    print(f"+++++++++++++++++++++ Bienvenido {nombre} +++++++++++++++++\n")
    print("  1. Agregar producto                 2. Mostrar productos  \n")
    print("  3. Buscar producto                  4. Eliminar producto  \n")
    print("  5. Stock Minimo                     6. SALIR              \n")
    print("------------------Ingrese la opción deseada-----------------")

def iniciar_sesion():
    texto = "| Iniciar Sesion (I) |  Registrarse  R  |      Salir  X      |"
    relleno(fondo,ancho)
    relleno(fondo,ancho)
    print(fondo + centrar_texto(texto, ancho))                                                      
    relleno(fondo,ancho)
    relleno(fondo,ancho) 

"""def menu_inicio(nombre="Usuario"):
    fondo = Back.LIGHTCYAN_EX + Fore.BLACK + Style.BRIGHT
    asteriscos = Fore.MAGENTA + "*" * 60

    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n" * 3)
    print(centrar_texto(asteriscos))
    print(centrar_texto(fondo + " PROGRAMA DE COMPRAS ONLINE ".center(60)))
    print(centrar_texto(asteriscos))
    print()
    print(centrar_texto(fondo + f"Bienvenido {nombre}".center(60)))
    print()
    print(centrar_texto(fondo + "1. Agregar producto    2. Mostrar productos".center(60)))
    print(centrar_texto(fondo + "3. Buscar producto     4. Eliminar producto".center(60)))
    print(centrar_texto(fondo + "5. SALIR".center(60)))
    print()
    print(centrar_texto(fondo + "Ingrese la opción deseada:".center(60)))"""