codigo = input("Ingrese código de salida (4 dígitos): ")

if len(codigo) == 4 and codigo.isdigit():
    dpto_code = codigo[0]
    hora = codigo[1:3]
    paradas_code = codigo[3]

    # Departamento
    if dpto_code == "1":
        dpto = "(T) TUMBES"
    elif dpto_code == "2":
        dpto = "(A) AREQUIPA"
    elif dpto_code == "3":
        dpto = "(P) PUNO"
    else:
        dpto = "Código de departamento inválido"

    # Paradas
    if paradas_code == "1":
        paradas = "(S) Sí"
    elif paradas_code == "2":
        paradas = "(N) No"
    else:
        paradas = "Código de paradas inválido"

    print("\nDepartamento de destino:", dpto)
    print("Hora de salida:", hora)
    print("Realizan paradas:", paradas)

else:
    print("Código inválido. Debe tener 4 dígitos numéricos.")



"""
Version con match-case (Python 3.10+)
"""
codigo = input("Ingrese código de salida (4 dígitos): ")

if len(codigo) == 4 and codigo.isdigit():
    dpto_code = codigo[0]
    hora = codigo[1:3]
    paradas_code = codigo[3]

    # Departamento (usando match-case)
    match dpto_code:
        case "1":
            dpto = "(T) TUMBES"
        case "2":
            dpto = "(A) AREQUIPA"
        case "3":
            dpto = "(P) PUNO"
        case _:
            dpto = "Código de departamento inválido"

    # Paradas (usando match-case)
    match paradas_code:
        case "1":
            paradas = "(S) Sí"
        case "2":
            paradas = "(N) No"
        case _:
            paradas = "Código de paradas inválido"

    print("\nDepartamento de destino:", dpto)
    print("Hora de salida:", hora)
    print("Realizan paradas:", paradas)

else:
    print("Código inválido. Debe tener 4 dígitos numéricos.")
