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

    nombre = input("Ingrese el nombre del producto vendido: ")
    cantidad_vendida = int(input("Ingrese la cantidad vendida: "))

    encontrado = False

    for producto in inventario:

        if producto["nombre"] == nombre:

            encontrado = True

            if producto["cantidad"] >= cantidad_vendida:

                producto["cantidad"] -= cantidad_vendida

                total = producto["precio"] * cantidad_vendida

                print("Venta realizada correctamente.")
                print("Total a pagar:", total)

            else:
                print("No hay suficiente cantidad en el inventario.")

    if encontrado == False:
        print("El producto no existe en el inventario.")


#mitad de ejercicio hecho

