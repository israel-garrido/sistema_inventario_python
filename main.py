# main.py
# Importación del módulo creado [cite: 35, 36]
import funciones_inventario as inv

def menu_principal():
    '''Función que muestra el menú y maneja la elección del usuario.'''
    # Uso de bucle WHILE para mantener el programa vivo [cite: 23]
    while True:
        print("\n=======================================")
        print(" SISTEMA DE GESTIÓN DE DATOS (INVENTARIO) ")
        print("=======================================")
        print("1. Agregar producto")
        print("2. Ver todos los productos")
        print("3. Calcular total de artículos (Recursivo)")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")

        # Uso de estructuras de control IF/ELIF/ELSE [cite: 22]
        if opcion == "1":
            inv.agregar_producto()
        
        elif opcion == "2":
            inv.ver_inventario()
            
        elif opcion == "3":
            # Llamamos a la función recursiva empezando desde el índice 0
            total = inv.sumar_inventario_recursivo(0)
            print(f"Total de artículos en inventario (cálculo recursivo): {total}")
            
        elif opcion == "4":
            print("Saliendo del sistema...")
            break # Uso de BREAK para romper el ciclo [cite: 24]
            
        else:
            print("Opción no válida, intente de nuevo.")

# Punto de arranque del script
if __name__ == "__main__":
    menu_principal()