"""
Escribe un programa que utilice un diccionario para almacenar factores de conversión
(ej: de metros a pies). Luego, crea una función que reciba una cantidad, la unidad de
origen y la unidad de destino, y realice la conversión. La función debe manejar el caso
en que una unidad no exista en el diccionario.
• Conceptos aplicados: Diccionarios, funciones con múltiples parámetros,
return, manejo de errores básicos con if key in dict.
"""
# Diccionario de conversión 
from math import e

# diccioonario de conversiones con unidades de longitud y sus factores de conversión entre sí

conversiones = {
    "metros": {
        "centimetros": 100,
        "kilometros": 0.001,
        "pies": 3.28084,
        "millas": 0.000621371
    },

    "centimetros": {
        "metros": 0.01,
        "kilometros": 0.00001,
        "pies": 0.0328084,
        "millas": 0.0000062137
    },

    "kilometros": {
        "metros": 1000,
        "centimetros": 100000,
        "pies": 3280.84,
        "millas": 0.621371
    },

    "pies": {
        "metros": 0.3048,
        "centimetros": 30.48,
        "kilometros": 0.0003048,
        "millas": 0.000189394
    },

    "millas": {
        "metros": 1609.34,
        "centimetros": 160934,
        "kilometros": 1.60934,
        "pies": 5280
    }
}



# Función para convertir

# funcion convertir que recibe una cantidad, la unidad de origen y la unidad de destino, y realiza la conversión 
# utilizando el diccionario de conversiones. La función también maneja el caso en que una unidad no exista en el diccionario, devolviendo un mensaje de error adecuado.
def convertir(cantidad, origen, destino):

    if origen in conversiones:

        if destino in conversiones[origen]:

            resultado = cantidad * conversiones[origen][destino]
            return resultado

        else:
            return "Error: la unidad de destino no existe."

    else:
        return "Error: la unidad de origen no existe."


# Mostrar unidades disponibles

print("UNIDADES DISPONIBLES:")
print("- metros")
print("- centimetros")
print("- kilometros")
print("- pies")
print("- millas")


# Entradas del usuario
# solicitamos al usuario que ingrese la cantidad a convertir, la unidad de origen y la unidad de
#  destino, y luego llamamos a la función convertir para realizar la conversión y mostrar el resultado.
cantidad = float(input("\nIngrese la cantidad: "))
origen = input("Ingrese la unidad de origen: ")
destino = input("Ingrese la unidad de destino: ")

# Conversión
# llamamos a la función convertir con los parámetros ingresados por el usuario y guardamos el resultado en la variable resultado
resultado = convertir(cantidad, origen, destino)

# Mostrar resultado
print("Resultado:", resultado, destino)
