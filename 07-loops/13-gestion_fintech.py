print("=== FinanCello Mini ===")

movements = {}  # Diccionario anidado para guardar movimientos
movement_id = 1
option = 0

while option != 6:

    print("\n--- MENU ---")
    print("1. Registrar ingreso")
    print("2. Registrar gasto")
    print("3. Mostrar movimientos")
    print("4. Mostrar saldo actual")
    print("5. Buscar movimiento por categoria")
    print("6. Salir")

    option = int(input("Elige una opcion: "))

    # OPCION 1: REGISTRAR INGRESO
    if option == 1:
        amount = float(input("Ingrese monto: "))
        category = input("Ingrese categoria: ")
        description = input("Ingrese descripcion: ")

        if amount > 0:
            movements[movement_id] = {
                "type": "income",
                "amount": amount,
                "category": category,
                "description": description
            }
            movement_id += 1
            print("Ingreso registrado correctamente!")
        else:
            print("Error: el monto debe ser mayor a 0")

    # OPCION 2: REGISTRAR GASTO
    elif option == 2:
        amount = float(input("Ingrese monto: "))
        category = input("Ingrese categoria: ")
        description = input("Ingrese descripcion: ")

        # Calcular saldo actual antes de registrar el gasto
        balance = 0
        for mov in movements.values():
            if mov["type"] == "income":
                balance += mov["amount"]
            else:
                balance -= mov["amount"]

        if amount > 0:
            if amount <= balance:
                movements[movement_id] = {
                    "type": "expense",
                    "amount": amount,
                    "category": category,
                    "description": description
                }
                movement_id += 1
                print("Gasto registrado correctamente!")
            else:
                print("Error: saldo insuficiente")
        else:
            print("Error: el monto debe ser mayor a 0")

    # OPCION 3: MOSTRAR MOVIMIENTOS (For anidado)
    elif option == 3:
        print("\n=== Lista de Movimientos ===")

        if len(movements) == 0:
            print("No hay movimientos registrados.")
        else:
            for mov_id, mov_info in movements.items():
                print(f"\nMovimiento ID: {mov_id}")

                for field, value in mov_info.items():
                    print(f"  {field}: {value}")

    # OPCION 4: MOSTRAR SALDO ACTUAL
    elif option == 4:
        balance = 0

        for mov in movements.values():
            if mov["type"] == "income":
                balance += mov["amount"]
            else:
                balance -= mov["amount"]

        print(f"Saldo actual: {balance}")

    # OPCION 5: BUSCAR MOVIMIENTO POR CATEGORIA
    elif option == 5:
        search_category = input("Ingrese categoria a buscar: ")

        found = False
        print("\n=== Resultados de Busqueda ===")

        for mov_id, mov_info in movements.items():
            if mov_info["category"].lower() == search_category.lower():
                print(f"\nMovimiento ID: {mov_id}")

                for field, value in mov_info.items():
                    print(f"  {field}: {value}")

                found = True

        if found == False:
            print("No se encontraron movimientos en esa categoria.")

    # OPCION 6: SALIR
    elif option == 6:
        print("Adios!")

    # OPCION INVALIDA
    else:
        print("Opcion invalida. Intente nuevamente.")
