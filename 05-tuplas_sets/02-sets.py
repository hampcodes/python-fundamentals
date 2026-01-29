# Set con distintos tipos de valores
my_set = {1, 2.5, "Hello", True, (1, 2, 3)}
print(my_set)

# Acceder a elementos (no se puede por índice, se usa in)
print("Hello" in my_set)  # Resultado: True
print(10 in my_set)  # Resultado: False

# Métodos de sets:

# .add() - Agrega un elemento al set
my_set.add("World")
print(my_set)

# .remove() - Elimina un elemento del set
my_set.remove(2.5)
print(my_set)

# .discard() - Elimina un elemento sin error si no existe
my_set.discard(100)
print(my_set)

# my_set = {1, [2, 3]}  # ESTO NO SE PUEDE - Las listas son mutables
# my_set = {1, {"key": "value"}}  # ESTO NO SE PUEDE - Los diccionarios son mutables