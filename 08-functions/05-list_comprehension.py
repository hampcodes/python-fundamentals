"""
Ejemplo  1: Filtrar y transformar a la vez
#Objetivo: de una lista de notas, quedarnos solo con las aprobadas y elevarlas al cuadrado.

Aquí hicimos 2 cosas a la vez:

filtramos (if n >= 11)

transformamos (n**2)
"""
notas = [5, 11, 14, 9, 18, 20, 7]

aprobadas_cuadrado = [n**2 for n in notas if n >= 11]

print(aprobadas_cuadrado)




"""
Ejemplo  2: Limpiar texto y quedarte con palabras válidas

Objetivo: limpiar palabras (minúsculas, sin espacios) y eliminar vacías.
usado en procesamiento de datos.
"""

palabras = [" Hola ", "Python", "  ", "Mundo", " ChatGPT ", ""]

limpias = [p.strip().lower() for p in palabras if p.strip() != ""]

print(limpias)


"""
Ejemplo  3: Extraer datos de diccionarios (tipo API JSON)

Objetivo: obtener solo los nombres de usuarios activos.
Esto se usa muchísimo en backend cuando recibes listas JSON.
"""

usuarios = [
    {"id": 1, "nombre": "Ana", "activo": True},
    {"id": 2, "nombre": "Luis", "activo": False},
    {"id": 3, "nombre": "Carlos", "activo": True}
]

activos = [u["nombre"] for u in usuarios if u["activo"]]

print(activos)



"""
Ejemplo 4: List comprehension con if-else (condición dentro)

Objetivo: convertir notas en texto: "Aprobado" o "Desaprobado"
Aquí el if-else está dentro de la expresión.
"""

notas = [8, 15, 10, 18]

resultado = ["Aprobado" if n >= 11 else "Desaprobado" for n in notas]

print(resultado)
