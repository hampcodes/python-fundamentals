prices = [25.5, 10.0, 7.99, 30.0, 15.0]
print(prices)

# sort(): ordena la lista original de menor a mayor
prices.sort()
print(prices)
# [7.99, 10.0, 15.0, 25.5, 30.0]

# sort(reverse=True): ordena de mayor a menor
prices.sort(reverse=True)
print(prices)
# [30.0, 25.5, 15.0, 10.0, 7.99]

print("-" * 30)

names = ['Luis', 'Ana', 'Pedro', 'María']
print(names)

# sorted(): devuelve una nueva lista ordenada (no modifica la original)
ordered_names = sorted(names)
print(ordered_names)
print(names)   # La lista original no cambia

print("-" * 30)

# reverse(): invierte el orden actual de la lista
names.reverse()
print(names)
