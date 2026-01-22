shopping_cart = ['Camisas', 'Tenis', 'Calcetas', 'Pantalones', 'Gorras']
print(shopping_cart)

# remove(x): elimina la primera aparición del valor indicado
shopping_cart.remove('Calcetas')
print(shopping_cart)
# ['Camisas', 'Tenis', 'Pantalones', 'Gorras']

# pop(i): elimina y devuelve el elemento en la posición i
removed_item = shopping_cart.pop(1)   # Elimina 'Tenis'
print(removed_item)                   # Tenis
print(shopping_cart)
# ['Camisas', 'Pantalones', 'Gorras']

# pop(): sin índice, elimina el último elemento
shopping_cart.pop()
print(shopping_cart)
# ['Camisas', 'Pantalones']

# clear(): elimina todos los elementos de la lista
shopping_cart.clear()
print(shopping_cart)
# []
