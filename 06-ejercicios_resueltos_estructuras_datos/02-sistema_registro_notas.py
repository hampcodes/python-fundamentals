"""
Ejercicio 2: Sistema de Registro de Notas
Justificación de la Estructura de Datos
Para este ejercicio utilizo una lista porque:

Necesitamos almacenar múltiples valores del mismo tipo (notas)
Las notas pueden agregarse dinámicamente durante la ejecución
Necesitamos recorrer todos los elementos para calcular el promedio
Podemos usar funciones como max(), min() y sum() directamente sobre listas
El orden importa (nota 1, nota 2, nota 3, etc.)

¿Por qué no otras estructuras?

Diccionario: No es necesario acceder a las notas por clave, solo procesarlas en conjunto
Tupla: Las notas se ingresan una por una y la tupla no permite agregar elementos
Set: Eliminaría notas duplicadas (si hay dos 15, solo guardaría uno) y perdería el orden
"""

# Entrada de datos
nombre = input("Ingrese nombre del estudiante: ")

# Almacenar notas en una lista
notas = []

nota1 = float(input("Ingrese nota 1: "))
notas.append(nota1)

nota2 = float(input("Ingrese nota 2: "))
notas.append(nota2)

nota3 = float(input("Ingrese nota 3: "))
notas.append(nota3)

nota4 = float(input("Ingrese nota 4: "))
notas.append(nota4)

nota5 = float(input("Ingrese nota 5: "))
notas.append(nota5)

# Calcular estadísticas
nota_alta = max(notas)
nota_baja = min(notas)
suma_notas = notas[0] + notas[1] + notas[2] + notas[3] + notas[4]
promedio = suma_notas / 5

# Determinar calificación
if promedio >= 16:
    calificacion = "Excelente"
elif promedio >= 11:
    calificacion = "Aprobado"
else:
    calificacion = "Desaprobado"

# Determinar observación
if nota_baja < 7:
    observacion = "Requiere refuerzo académico"
else:
    observacion = "Ninguna"

# Mostrar reporte
print("=" * 50)
print("           REPORTE DE CALIFICACIONES")
print("=" * 50)
print(f"Estudiante: {nombre}")
print("-" * 50)
print("Notas registradas:")
print(f"  Nota 1: {notas[0]}")
print(f"  Nota 2: {notas[1]}")
print(f"  Nota 3: {notas[2]}")
print(f"  Nota 4: {notas[3]}")
print(f"  Nota 5: {notas[4]}")
print("-" * 50)
print(f"Nota más alta: {nota_alta}")
print(f"Nota más baja: {nota_baja}")
print(f"Promedio: {promedio:.2f}")
print(f"Calificación: {calificacion}")
print("-" * 50)
print(f"Observación: {observacion}")
print("=" * 50)