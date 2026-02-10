"""
LIST COMPREHENSION - ¿QUÉ ES Y CUÁNDO SE USA?

Una List Comprehension es una forma corta de crear una lista en Python.
Reemplaza un for tradicional y permite escribir código más compacto y claro.

Se usa principalmente cuando necesitas:
- Transformar datos (ej: elevar números, convertir texto, aplicar funciones)
- Filtrar datos (ej: quedarte solo con aprobados)
- Extraer información de diccionarios o JSON (ej: obtener nombres de usuarios)

----------------------------------------------------------
SINTAXIS 1: TRANSFORMAR (solo for)
[expresion for elemento in lista]

Ejemplo:
[n**2 for n in notas]

Aquí:
- "n**2" es la expresión (lo que se guarda en la lista nueva)
- "for n in notas" recorre la lista original

----------------------------------------------------------
SINTAXIS 2: FILTRAR (if al final)
[expresion for elemento in lista if condicion]

Ejemplo:
[n for n in notas if n >= 11]

Aquí:
- el if al final filtra (solo entra si cumple la condición)

----------------------------------------------------------
SINTAXIS 3: DECISIÓN (if-else dentro)
[valor_si_true if condicion else valor_si_false for elemento in lista]

Ejemplo:
["Aprobado" if n >= 11 else "Desaprobado" for n in notas]

Aquí:
- no se filtra nada
- todos entran, pero el valor cambia según la condición

REGLA RÁPIDA:
- Si hay ELSE, el IF va antes.
- Si no hay ELSE, el IF va al final (filtro).
"""



"""
Ejemplo 1: Filtrar y transformar a la vez
Objetivo: quedarnos solo con las notas aprobadas (>=11) y elevarlas al cuadrado.
"""

notas = [5, 11, 14, 9, 18, 20, 7]

# SIN LIST COMPREHENSION (versión tradicional)
# aprobadas_cuadrado = []
# for n in notas:
#     if n >= 11:
#         aprobadas_cuadrado.append(n**2)

# LIST COMPREHENSION: filtra aprobadas y genera su cuadrado
aprobadas_cuadrado = [n**2 for n in notas if n >= 11]

print("Notas aprobadas al cuadrado:", aprobadas_cuadrado)




"""
Ejemplo 2: Limpiar texto y quedarte con palabras válidas
Objetivo: eliminar espacios, pasar a minúscula y descartar cadenas vacías.

strip() elimina espacios al inicio y al final.
lower() convierte el texto a minúscula.
"""

palabras = [" Hola ", "Python", "  ", "Mundo", " ChatGPT ", ""]

# SIN LIST COMPREHENSION (versión tradicional)
# limpias = []
# for p in palabras:
#     palabra = p.strip()
#     if palabra != "":
#         limpias.append(palabra.lower())

# LIST COMPREHENSION: limpia texto y filtra vacíos
limpias = [p.strip().lower() for p in palabras if p.strip() != ""]

print("Palabras limpias:", limpias)




"""
Ejemplo 3: Extraer datos de diccionarios (tipo API JSON)
Objetivo: obtener solo los nombres de usuarios activos.
"""

usuarios = [
    {"id": 1, "nombre": "Ana", "activo": True},
    {"id": 2, "nombre": "Luis", "activo": False},
    {"id": 3, "nombre": "Carlos", "activo": True}
]

# SIN LIST COMPREHENSION (versión tradicional)
# activos = []
# for u in usuarios:
#     if u["activo"] == True:
#         activos.append(u["nombre"])

# LIST COMPREHENSION: filtra usuarios activos y extrae el nombre
activos = [u["nombre"] for u in usuarios if u["activo"]]

print("Usuarios activos:", activos)




"""
Ejemplo 4: List comprehension con if-else (decisión dentro)
Objetivo: generar una lista de resultados ("Aprobado" o "Desaprobado") para cada nota.
"""

notas = [8, 15, 10, 18]

# SIN LIST COMPREHENSION (versión tradicional)
# resultado = []
# for n in notas:
#     if n >= 11:
#         resultado.append("Aprobado")
#     else:
#         resultado.append("Desaprobado")

# LIST COMPREHENSION: genera el texto según la condición (no filtra)
resultado = ["Aprobado" if n >= 11 else "Desaprobado" for n in notas]

print("Estado de cada nota:", resultado)


"""
Ejemplo 5 (Potente): Aplanar listas (flatten) y filtrar datos
Objetivo: de una lista de listas (notas por alumno), obtener una sola lista con todas las notas aprobadas.

Este caso es muy usado cuando tienes datos agrupados (ej: por alumno, por curso, por semanas).
"""
notas_por_alumno = {
    "Ana": [10, 15, 18],
    "Luis": [20, 8, 12],
    "Carlos": [14, 9, 11]
}
# SIN LIST COMPREHENSION
# aprobadas = []
# for alumno, notas in notas_por_alumno.items():
#     for n in notas:
#         if n >= 11:
#             aprobadas.append(n)

# LIST COMPREHENSION: recorre alumnos, recorre sus notas y filtra aprobadas
aprobadas = [n for alumno, notas in notas_por_alumno.items() for n in notas if n >= 11]

print(aprobadas)
