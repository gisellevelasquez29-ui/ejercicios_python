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

# Variable de control
opcion = ""

while opcion != "4":

    print("\n--- MENÚ DE COMPRAS ---")
    print("1. Agregar ítem")
    print("2. Eliminar ítem")
    print("3. Ver lista completa")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        item = input("Ingrese el nombre del ítem: ")
        lista_compras.append(item)
        print("Ítem agregado correctamente.")

    elif opcion == "2":
        item = input("Ingrese el ítem a eliminar: ")

        if item in lista_compras:
            lista_compras.remove(item)
            print("Ítem eliminado correctamente.")
        else:
            print("El ítem no está en la lista.")

    elif opcion == "3":
        print("\nLista de compras:")

        if len(lista_compras) == 0:
            print("La lista está vacía.")
        else:
            for item in lista_compras:
                print("lista")
                print("-", item)

    elif opcion == "4":
        print("Programa finalizado.")

    else:
        print("Opción inválida.")