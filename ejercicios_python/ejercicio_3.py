# Ejercicio 3 : agenda de contactos con diccionario

# creamos un diccionario vacio para guardar los contactos 
agenda_contactos = {}


# --- 2. Definición de Funciones ---

# función para añadir un nuevo contacto al diccionario, solicitando el nombre y el teléfono al usuario
def añadir_contacto():
    """Solicita un nombre y un teléfono para agregarlos a la agenda."""
    print("\n--- Añadir Nuevo Contacto ---")
    nombre = input("Ingresa el nombre del contacto: ").strip()
    
    # Validamos que el nombre no esté vacío
    if not nombre:
        print("❌ El nombre no puede estar vacío.")
        return

    telefono = input(f"Ingresa el número de teléfono de {nombre}: ").strip()
    
    
    # Añadir o actualizar en el diccionario
    # variable nombre es la clave y telefono es el valor, si el nombre ya existe se actualiza el telefono, si no existe se agrega un nuevo contacto
    agenda_contactos[nombre] = telefono
    print(f"✅ Contacto '{nombre}' guardado con éxito.")


# función para buscar un contacto por su nombre, solicitando el nombre al usuario y mostrando el teléfono si el contacto existe en el diccionario
def buscar_contacto():
    """Busca un contacto por su nombre en el diccionario."""
    print("\n--- Buscar Contacto ---")
    nombre_buscar = input("Ingresa el nombre del contacto que buscas: ").strip()
    
    # Verificamos si la clave existe en el diccionario
    if nombre_buscar in agenda_contactos:
        # agenda contactos[nombre_buscar] devuelve el valor asociado a la clave nombre_buscar, que es el teléfono del contacto
        print(f"📞 Teléfono de {nombre_buscar}: {agenda_contactos[nombre_buscar]}")
    else:
        print(f"❌ El contacto '{nombre_buscar}' no se encuentra en la agenda.")


# funcion mostrar contacto 
def mostrar_contactos():
    """Muestra la lista completa de contactos usando un bucle for."""
    print("\n--- Lista de Contactos ---")
    
    # Verificamos si el diccionario está vacío
    # if not agenda_contactos: verifica si el diccionario agenda_contactos no tiene elementos, es decir, está vacío.
    #  Si está vacío, se muestra un mensaje indicando que la agenda está vacía y se retorna para salir de la función.
    if not agenda_contactos:
        print("La agenda está vacía.")
        # return se utiliza para salir de la opcion evitando que el programa continue con el bucle for, ya que no hay contactos para mostrar
        return
    
    # Bucle for para iterar sobre los elementos del diccionario (clave, valor)
    for nombre, telefono in agenda_contactos.items():
        print(f"👤 Nombre: {nombre} | 📞 Teléfono: {telefono}")


# --- 3. Menú Principal Interactiva ---

# bucle while para mostras el menu principal y un if / elif / else para gestionar las opciones del usuario, 
# llamando a las funciones correspondientes según la opción seleccionada
def menu():
    while True:
        print("\n=============================")
        print("    AGENDA DE CONTACTOS")
        print("=============================")
        print("1. Añadir un nuevo contacto")
        print("2. Buscar teléfono por nombre")
        print("3. Mostrar todos los contactos")
        print("4. Salir")
        
        opcion = input("Selecciona una opción (1-4): ").strip()
        
        if opcion == "1":
            añadir_contacto()
        elif opcion == "2":
            buscar_contacto()
        elif opcion == "3":
            mostrar_contactos()
        elif opcion == "4":
            print("👋 Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida. Por favor, selecciona un número del 1 al 4.")

# Ejecutar el programa principal
# llamamos a la función menu para iniciar el programa y mostrar el menú principal al usuario
menu()