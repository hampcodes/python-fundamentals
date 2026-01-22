# Matriz: filas = sucursales, columnas = productos
inventory = [
    [10, 5, 2],   # Sucursal 1: camisas, pantalones, zapatos
    [7, 8, 4],    # Sucursal 2
    [3, 6, 9]     # Sucursal 3
]

# Acceder a un valor específico (Sucursal 2, producto 1)
print(inventory[1][0])   # 7

# Modificar un valor (Sucursal 1, producto 2)
inventory[0][1] = 12

# Mostrar la matriz completa
print(inventory)
