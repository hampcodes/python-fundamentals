# ==============================
# Métodos de adición con NÚMEROS (precios)
# ==============================

prices = [10.5, 25.0, 7.99]
print(prices)

# append(): agrega UN solo elemento al final de la lista
prices.append(15.0)
prices.append(30.0)

# insert(pos, valor): agrega un elemento en una posición específica
prices.insert(1, 12.5)   # Inserta 12.5 en la posición 1
prices.insert(3, 18.0)   # Inserta 18.0 en la posición 3

# extend(lista): agrega varios elementos de otra lista al final
prices.extend([5.0, 9.99, 20.0])

print(prices)




# ==============================
# Métodos de adición con STRINGS
# ==============================

shopping_cart = ['Camisas', 'Tenis', 'Calcetas']
print(shopping_cart)

# append(): agrega un solo elemento al final
shopping_cart.append('Pantalones')
print(shopping_cart)

# insert(): agrega un elemento en una posición específica
shopping_cart.insert(1, 'Gorras')
print(shopping_cart)

# extend(): agrega varios elementos de otra lista
new_items = ['Polos', 'Casacas']
shopping_cart.extend(new_items)
print(shopping_cart)
