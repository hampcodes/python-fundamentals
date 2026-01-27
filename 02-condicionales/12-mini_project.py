# Entradas
# strip() elimina espacios en blanco al inicio y al final
# upper() convierte todo a mayúsculas para evitar errores por minúsculas
marca = input("Ingrese marca (B=Best, M=Monark, O=Oxford): ").strip().upper()
categoria = input("Ingrese categoría (P=Paseo, M=Montañera): ").strip().upper()

precio = None

# Validar marca
if marca in ["B", "M", "O"]:

    # Validar categoría
    if categoria in ["P", "M"]:

        match marca:
            case "B":  # Best
                match categoria:
                    case "P":
                        precio = 1300
                    case "M":
                        precio = 1000

            case "M":  # Monark
                match categoria:
                    case "P":
                        precio = 1350
                    case "M":
                        precio = 2500

            case "O":  # Oxford
                match categoria:
                    case "P":
                        precio = 900
                    case "M":
                        precio = 3200

    else:
        print("Categoría inválida. Use P o M.")

else:
    print("Marca inválida. Use B, M u O.")

# Salida
if precio is not None:
    print("El monto a pagar es: S/.", precio)
