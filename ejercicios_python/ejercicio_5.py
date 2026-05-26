"""
Diseña un sistema para gestionar el inventario de una tienda. El inventario se
almacenará en una lista de diccionarios. Cada diccionario representará un
producto con "nombre", "precio" y "cantidad". El programa debe:
• Usar funciones para cada operación: agregar_producto(), realizar_venta(),
mostrar_inventario().
• La función realizar_venta() debe actualizar la cantidad del producto vendido.
• Mostrar un menú interactivo para el usuario.
• Conceptos integrados: Listas, diccionarios, funciones, bucles,
condicionales.
"""

# Lista donde se guardará el inventario
inventario = []


# Función para agregar productos

def agregar_producto():
    
    # ingresamos el nombre, precio y cantidad del producto a agregar al inventario, luego creamos un diccionario con esa información y lo agregamos
    #  a la lista de inventario, finalmente indicamos al usuario que el producto se agregó correctamente.
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    inventario.append(producto)

    print("Producto agregado correctamente.")


# Función para realizar una venta

def realizar_venta():
    # solicictamos incresar el nombre de producto vendido y su cantidad 

    nombre = input("Ingrese el nombre del producto vendido: ")
    cantidad_vendida = int(input("Ingrese la cantidad vendida: "))



    encontrado = False

    # un for para verificar si el producto existe en el inventario 

    for producto in inventario:

        if producto["nombre"] == nombre:

            # si es verdadero

            encontrado = True
            # se verifica si hay suficiente cantida en el inventario 

            if producto["cantidad"] >= cantidad_vendida:

                # si hay suficienta cantidad se le restara la cantidad vendida al producto del inventario 

                producto["cantidad"] -= cantidad_vendida

                # se calcula el total a pagar multiplicando el precio del producto por la cantidad vendida 

                total = producto["precio"] * cantidad_vendida

                # se indica al usuario que la venta se realizo correctamente y el total a pagar

                print("Venta realizada correctamente.")
                print("Total a pagar:", total)

                # si no hay suficiente cantidad se le indica al usuario que no hay suficiente cantidad en el inventario

            else:
                print("No hay suficiente cantidad en el inventario.")
        
    # si el producto no se encuentra en el inventario se le indica al usuario que el producto no existe 

    if encontrado == False:
        print("El producto no existe en el inventario.")



# Función para mostrar el inventario
def mostrar_inventario():

    # si el inventario el = 0 se indica que el inventario esta vacio 

    if len(inventario) == 0:
        print("El inventario está vacío.")

        # si el inventari no esta vacio se muestra el nombre del los productos 

    else:
        print("\n--- INVENTARIO ---")

        for producto in inventario:

            print(
                "Nombre:", producto["nombre"],
                "| Precio:", producto["precio"],
                "| Cantidad:", producto["cantidad"]
            )


# Menú interactivo

# bucle while con un if / elif / else para mostrar el menú principal y gestionar las opciones , 
# llamando a las funciones correspondientes según la opción seleccionada, y permitiendo salir del programa cuando el usuario lo desee.


while True:

    print("\n===== MENÚ =====")
    print("1. Agregar producto")
    print("2. Realizar venta")
    print("3. Mostrar inventario")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        agregar_producto()

    elif opcion == "2":

        realizar_venta()

    elif opcion == "3":

        mostrar_inventario()

    elif opcion == "4":

        print("Programa finalizado.")
        break

    else:
        print("Opción no válida. Intente nuevamente.")