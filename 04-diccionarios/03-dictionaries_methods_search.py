user = {
    'name': 'Henry',
    'age': 29,
    'greet': 'Hola Mundo',
    'numbers': [1, 2, 3]
}

# .get()
print(user.get('name'))        # Henry (existe)
print(user.get('email'))       # None (no existe)
print(user.get('email', 'No registrado'))  # Valor por defecto

# in sobre claves
print('name' in user)          # True
print('email' in user)         # False

# in sobre valores
print(user.values())
print('Henry' in user.values())     # True
print('Hola Mundo' in user.values())  # True

# in sobre pares (clave, valor)
print(user.items())
print(('age', 29) in user.items())    # True
print(('age', 30) in user.items())    # False
