# Ejercicio 1 : analisis de calificaciones en una lista 

# Lista de calificaciones
calificaciones = [4.5, 3.8, 5.0, 2.9, 4.2]

# Función
def analizar_calificaciones(lista):

    promedio = sum(lista) / len(lista)
    mayor = max(lista)
    menor = min(lista)

    return (promedio, mayor, menor)

# Probar función
resultado = analizar_calificaciones(calificaciones)

print("Promedio:", resultado[0])
print("Calificación más alta:", resultado[1])
print("Calificación más baja:", resultado[2])