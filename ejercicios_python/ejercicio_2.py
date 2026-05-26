"""
Desarrolla un programa que permita al usuario gestionar una lista de compras. El
programa debe usar un bucle while para mostrar un menú con opciones:
1. Agregar ítem a la lista.
2. Eliminar ítem de la lista.
3. Verla lista completa.
4. Salir. El programa debe gestionar la lista de compras y seguir las
instrucciones del usuario.
• Conceptos aplicados: Listas (métodos append, remove), bucle while,
if/elif/else, input().
"""

# Crear lista vacía
lista_compras = []

# Variable de opción para el menú
opcion = ""

# bucle while para mostrar el menú hasta que el usuario decida salir (opción 4)
while opcion != "4":

    print("\n--- MENÚ DE COMPRAS ---")
    print("1. Agregar ítem")
    print("2. Eliminar ítem")
    print("3. Ver lista completa")
    print("4. Salir")

# Solicitar al usuario que ingrese una opción
    opcion = input("Seleccione una opción: ")

# si el usuario digita la opicion 1 se le solicita ingresar el nompre del articulo al final de la lista y se indica que el articulo  se agrego corectamente
    if opcion == "1":
        item = input("Ingrese el nombre del ítem: ")
        lista_compras.append(item)
        print("Ítem agregado correctamente.")

# si el usuario digita la opicion 2 se le solicita ingresar el nompre del articulo a eliminar de la lista y se
#  indica que el articulo se elimino corectamente, si el articulo no esta en la lista se le indica al usuario que el articulo no esta en la lista
    elif opcion == "2":
        item = input("Ingrese el ítem a eliminar: ")

        if item in lista_compras:
            lista_compras.remove(item)
            print("Ítem eliminado correctamente.")
        else:
            print("El ítem no está en la lista.")

# si el usuario digita la opicion 3 se muestra la lista completa de compras, si la lista esta vacia se le indica al usuario que la lista esta vacia
    elif opcion == "3":
        print("\nLista de compras:")

        if len(lista_compras) == 0:
            print("La lista está vacía.")
        else:
            for item in lista_compras:
                print("lista")
                print("-", item)

# si el usuario digita la opicion 4 se le indica que el programa finalizo
    elif opcion == "4":
        print("Programa finalizado.")

# si el usuario digita una opcion diferente a 1, 2, 3 o 4 se le indica que la opcion es invalida
    else:
        print("Opción inválida.")