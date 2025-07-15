# Módulo principal
import Interfas
import Programacion
import BaseDatos


BaseDatos.conexion_base_datos()  # Me vinculo a la base de datos de los Productos
BaseDatos.conexion_usuarios()    # Creo y vinculo la base de datos de los Usuarios
Interfas.mensaje_bienvenida()   
while True:  
    usuario = Programacion.iniciar_sesion()        # Registro, creo o inicio con usuario creado
    # Menú principal 
    while True:
        Interfas.menu_inicio(usuario)
        opcion = Programacion.elegir_menu()

        match opcion:
            case "1":
                Programacion.agregar_producto()
            case "2":
                Programacion.mostrar_productos()
            case "3":
                Programacion.buscar_producto()
            case "4":
                Programacion.eliminar_producto()
            case "5":
                Programacion.reporte_stock()
            case "6":
                Programacion.cerrando_programa()
            case _:
                Interfas.limpiar_pantalla()
                Interfas.estilo("Opción no válida.")
                Interfas.estilo("Presione Enter para continuar...")
                input()

