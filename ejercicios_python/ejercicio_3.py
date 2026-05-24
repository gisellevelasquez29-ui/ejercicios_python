# Ejercicio 3 : agenda de contactos con diccionario

# Diccionario de contactos
contactos = {}

# Función para agregar contacto
def agregar_contacto(nombre, telefono):
    contactos[nombre] = telefono
    print("Contacto agregado correctamente")

# Función para buscar contacto
def buscar_contacto(nombre):

    if nombre in contactos:
        print("Teléfono:", contactos[nombre])
    else:
        print("El contacto no existe")

# Función para mostrar contactos
def mostrar_contactos():

    print("\nLista de contactos")

    for nombre, telefono in contactos.items():
        print(nombre, ":", telefono)

# Agregar contactos
agregar_contacto("Laura", "3104567890")
agregar_contacto("Carlos", "3209876543")
agregar_contacto("Ana", "3001234567")

# Buscar contacto
buscar_contacto("Carlos")

# Mostrar todos los contactos
mostrar_contactos()