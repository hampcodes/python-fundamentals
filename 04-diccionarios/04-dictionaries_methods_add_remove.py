user = {
    'name': 'Fernando',
    'age': 29,
    'greet': 'Hola Mundo',
    'numbers': [1, 2, 3]
}

print("Diccionario original:", user)
print()

# 1. copy() → crear una copia independiente
user_copy = user.copy()
user_copy['age'] = 20   # solo cambia en la copia
print("Después de copy():")
print("Original:", user)
print("Copia:", user_copy)
print()

# 2. pop() → eliminar una clave específica
user.pop('age')
print("Después de pop('age'):", user)
print()

# 3. popitem() → eliminar el último par (clave, valor)
user.popitem()
print("Después de popitem():", user)
print()

# 4. update() → actualizar y agregar claves
user.update({'name': 'Henry'})  # actualiza una clave existente
user.update({'cats': 2})           # agrega una nueva clave
print("Después de update():", user)
print()

# 5. append() sobre una lista dentro del diccionario
user['skills'] = user.get('skills', [])  # crea la lista si no existe
user['skills'].append('Python')
user['skills'].append('Django')

print("Después de append en 'skills':", user)

# Mostrar nombre + skills
print("Nombre:", user.get("name"), "| Skills:", user["skills"])
