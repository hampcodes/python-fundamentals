# Tipos de datos

# String (Cadenas de texto, texto): guarda palabras o frases
nombre = "Henry"
apellido = "Mendoza"
saludo = "Hola Mundo"

# int (enteros): guarda números sin decimales
numero = 2000
edad = 29
gatos = 5

# float (Flotantes, decimales): guarda números con decimales
decimal = 20.42
temperatura = 27.3

# complex (Complejos): números con parte real e imaginaria
# Se usan en matemáticas, ingeniería, física y señales
numero_complejo1 = 2j          # solo parte imaginaria
numero_complejo2 = 3 + 5j      # parte real + parte imaginaria

# bool (Booleanos): guarda verdadero o falso
booleano = True
booleano_falso = False
is_gamer = True

# Datos especiales (estructuras de datos)

# Listas (arrays): guarda varios valores ordenados y modificables
# Se usan cuando necesitas agregar, quitar o cambiar valores
lista = [1, 2, 3]
lista_abc = ['a', 'b', 'c']

# Tupla: guarda varios valores ordenados pero no modificables
# Se usan para datos fijos que no deben cambiar
tupla = (1, 2, 3)

# Set: guarda valores únicos sin orden y sin posiciones fijas
# Se usan para eliminar duplicados o hacer comparaciones de conjuntos
set_variable = {1, 2, 3}

# Diccionario: guarda pares clave–valor
# Se usan para representar información con campos (como registros)
diccionario = {
    'hello': 'hola',
    'bye': 'adiós'
}

# Diccionario con datos mezclados: guarda información relacionada con distintos tipos de datos
# Se usa para agrupar datos de una persona, producto, etc.
informacion_personal = {
    'name': 'Ricardo',
    'age': 29,
    'cats': 5
}

# TODO EN PYTHON ES UN OBJETO: todo tiene un tipo y métodos
print(edad)
print(type(edad))

# Usa un método de string: convierte a mayúsculas
print(nombre.upper())
