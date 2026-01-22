shopping_cart = ['Camisas', 'Tenis', 'Calcetas', 'Pantalones', 'Gorras', 'Polos']

# Desde el índice 1 hasta el 4 (sin incluir el 4)
print(shopping_cart[1:4])   
# ['Tenis', 'Calcetas', 'Pantalones']

# Desde el inicio hasta el índice 3
print(shopping_cart[:3])    
# ['Camisas', 'Tenis', 'Calcetas']

# Desde el índice 2 hasta el final
print(shopping_cart[2:])    
# ['Calcetas', 'Pantalones', 'Gorras', 'Polos']

# Copiar toda la lista
new_cart = shopping_cart[:]
print(new_cart)             
# ['Camisas', 'Tenis', 'Calcetas', 'Pantalones', 'Gorras', 'Polos']

# Usando saltos (step)
print(shopping_cart[::2])  
# ['Camisas', 'Calcetas', 'Gorras']

# Revertir la lista
print(shopping_cart[::-1])  
# ['Polos', 'Gorras', 'Pantalones', 'Calcetas', 'Tenis', 'Camisas']


#slicing en strings (también funciona igual)
text = "Programación"

print(text[0:7])     # 'Programa'
print(text[:4])      # 'Prog'
print(text[4:])      # 'ramación'
print(text[::-1])    # 'nóicamargorP'
