# Ejercicio 1 : analisis de calificaciones en una lista 

# Lista de calificaciones

#primeramente creamos una variable para distintas calificaciones
calificaciones = [4.5, 3.8, 5.0, 2.9, 4.2]

# Función
# luego definimos la función donde hacemos la operación para calcular el promedioy escoger la nota mayor o menor
def analizar_calificaciones(lista):

    promedio = sum(lista) / len(lista)
    mayor = max(lista)
    menor = min(lista)

 #finalmente retornamos el resultado de las operaciones en una tupla
#indices de la tupla: 0 = promedio, 1 = mayor, 2 = menor
    return (promedio, mayor, menor)

# Probar función
# después llamamos a la función para que aga las operaciones con las calificacviones y guardamos el resultado en una variable
resultado = analizar_calificaciones(calificaciones)

# imprimimos el resultado de las operaciones por medio de la variable resultado, indicando que indice corresponde a cada operación
print("Promedio:", resultado[0])
print("Calificación más alta:", resultado[1])
print("Calificación más baja:", resultado[2])