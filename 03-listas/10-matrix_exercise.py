# Matriz de asientos del bus
# Cada FILA representa una fila del bus
# Cada COLUMNA representa un asiento dentro de esa fila
bus_seats = [
    ['Libre', 'Ocupado', 'Libre'],   # Fila 0 → asientos 0, 1, 2
    ['Ocupado', 'Libre', 'Libre'],   # Fila 1 → asientos 0, 1, 2
    ['Libre', 'Libre', 'Ocupado']    # Fila 2 → asientos 0, 1, 2
]


print("Sistema de reservas de asientos - Bus")
print("Opciones:")
print("1. Ver estado de un asiento")
print("2. Reservar un asiento")
print("3. Mostrar todos los asientos")

option = input("Elige una opción (1-3): ")

if option == "1":
    fila = int(input("Ingresa la fila (0-2): "))
    asiento = int(input("Ingresa el asiento (0-2): "))
    print("Estado del asiento:", bus_seats[fila][asiento])

elif option == "2":
    fila = int(input("Ingresa la fila (0-2): "))
    asiento = int(input("Ingresa el asiento (0-2): "))

    if bus_seats[fila][asiento] == "Libre":
        bus_seats[fila][asiento] = "Ocupado"
        print("Asiento reservado correctamente")
    else:
        print("El asiento ya está ocupado")

elif option == "3":
    print("Estado actual de los asientos:")
    print(bus_seats)

else:
    print("Opción no válida")

print("Matriz final de asientos:")
print(bus_seats)
