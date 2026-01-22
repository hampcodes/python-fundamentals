# == Equal o igualdad

print(5 == 5)
print(True == 1)
print("" == 1)
print([] == 1)
print(10 == 10.1)

new_list = []
other_list = []

# is compara en memoria 0x1234ab
print(new_list is other_list)
print(new_list == other_list)

# Línea separadora solo para ordenar la salida en consola (no tiene que ver con is ni ==)
print("-" * 40)

# None: ausencia de valor (siempre se compara con is)
x = None
print(x is None)
