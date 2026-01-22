# Genera una lista de números del 0 al 199
numbers = list(range(200))

# Une una lista de palabras en una sola oración usando un espacio como separador
sentence = ' '.join(['Hola', 'Mundo', 'desde', 'un', 'join,', 'besos'])

# Ejemplo 1 de join: usar un espacio como separador
words = ['Aprender', 'Python', 'es', 'genial']
sentence1 = ' '.join(words)

# Ejemplo 2 de join: usar coma y espacio como separador
fruits = ['Manzana', 'Pera', 'Uva']
sentence2 = ', '.join(fruits)

# Calcula la suma total de los números
total = sum(numbers)

# Obtiene el número mayor de la lista
mayor = max(numbers)

# Obtiene el número menor de la lista
menor = min(numbers)

# Cuenta cuántos elementos tiene la lista
elements = len(numbers)

print("Total:", total)
print("Mayor:", mayor)
print("Menor:", menor)
print("Cantidad de elementos:", elements)
print("Oración original:", sentence)
print("Oración join con espacio:", sentence1)
print("Oración join con coma:", sentence2)
