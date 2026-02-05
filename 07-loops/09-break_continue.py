print("=== BREAK Example ===")

# BREAK: detiene el ciclo completamente
for item in [1, 2, 3, 4, 5]:
    if item == 4:
        break  # sale del ciclo cuando encuentra el 4
    print(item)


print("\n=== CONTINUE Example ===")

# CONTINUE: salta la iteración actual y continúa con la siguiente
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number == 3:
        continue  # no imprime el 3 y sigue con el siguiente número
    print(number)
