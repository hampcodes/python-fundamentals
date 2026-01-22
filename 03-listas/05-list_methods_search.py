shopping_cart = ['Camisas', 'Tenis', 'Calcetas', 'Pantalones', 'Tenis']
print(shopping_cart)

# index(x): devuelve la posición del primer elemento encontrado
pos = shopping_cart.index('Tenis')
print(pos)   # 1

# count(x): cuenta cuántas veces aparece un valor en la lista
total_tenis = shopping_cart.count('Tenis')
print(total_tenis)   # 2

# in: verifica si un valor existe en la lista
print('Camisas' in shopping_cart)   # True
print('Gorras' in shopping_cart)    # False
