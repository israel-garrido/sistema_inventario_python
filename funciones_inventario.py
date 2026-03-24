# funciones_inventario.py

# 1. Estructuras de datos globales
lista_productos = []
CATEGORIAS_DISPONIBLES = ("Electronica", "Hogar", "Ropa", "Alimentos")
nombres_registrados = set()

def mostrar_categorias():
    '''Muestra las categorías numeradas.'''
    print("--- Seleccione una Categoría ---")
    indice = 1
    for cat in CATEGORIAS_DISPONIBLES:
        print(f"{indice}. {cat}")
        indice += 1

def agregar_producto():
    '''
    Función para capturar datos. 
    Usa bucles while para obligar a ingresar datos numéricos válidos.
    '''
    print("\n--- Registrar Nuevo Producto ---")
    
    # Nombre en MAYÚSCULAS
    nombre = input("Ingrese el nombre del producto: ").strip().upper()
    
    if nombre in nombres_registrados:
        print("¡Error! Este producto ya existe.")
        return

    # --- CAMBIO AQUÍ: Validación persistente del Precio ---
    precio = 0.0
    while True:
        try:
            precio = float(input("Ingrese el precio: "))
            break # Si funciona, rompe el ciclo y avanza
        except ValueError:
            print("Error: El precio debe ser un número. Intente de nuevo.")

    # --- CAMBIO AQUÍ: Validación persistente de la Cantidad ---
    cantidad = 0
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad: "))
            break # Si funciona, rompe el ciclo y avanza
        except ValueError:
            print("Error: La cantidad debe ser un número entero. Intente de nuevo.")

    # Selección de categoría por número
    mostrar_categorias()
    
    categoria = ""
    while True:
        try:
            seleccion = int(input("Ingrese el número de la categoría: "))
            
            if seleccion >= 1 and seleccion <= len(CATEGORIAS_DISPONIBLES):
                categoria = CATEGORIAS_DISPONIBLES[seleccion - 1]
                break # Categoría válida, salimos del ciclo
            else:
                print(f"Error: Debe elegir un número entre 1 y {len(CATEGORIAS_DISPONIBLES)}.")
                
        except ValueError:
            print("Error: Debe ingresar un número entero.")

    # Creación del diccionario y guardado
    nuevo_producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
        "categoria": categoria
    }

    lista_productos.append(nuevo_producto)
    nombres_registrados.add(nombre)
    print(f"¡Producto '{nombre}' guardado con éxito en la sección {categoria}!")

def ver_inventario():
    '''Recorre la lista de productos y los muestra.'''
    print("\n--- Lista de Productos ---")
    if len(lista_productos) == 0:
        print("El inventario está vacío.")
    else:
        for producto in lista_productos:
            print(f"Producto: {producto['nombre']} | Precio: ${producto['precio']} | Stock: {producto['cantidad']} | Cat: {producto['categoria']}")

def sumar_inventario_recursivo(indice):
    '''
    Función recursiva para calcular el total de productos.
    '''
    if indice == len(lista_productos):
        return 0
    
    cantidad_actual = lista_productos[indice]["cantidad"]
    return cantidad_actual + sumar_inventario_recursivo(indice + 1)