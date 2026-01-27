# Ingreso de datos
"""
Ingrese zona (1–2): 2  
Ingrese consumo: 245  
El monto a pagar es: 156.5 soles  
"""
zona = int(input("Ingrese zona (1-2): "))
consumo = float(input("Ingrese consumo: "))

monto = 0

if zona == 1:  # Zona Comercial
    monto = 50
    if consumo <= 100:
        monto += consumo * 0.75
    else:
        monto += 100 * 0.75
        monto += (consumo - 100) * 0.90

elif zona == 2:  # Zona Residencial
    monto = 25
    if consumo <= 100:
        monto += consumo * 0.30
    else:
        monto += 100 * 0.30
        monto += (consumo - 100) * 0.70

else:
    print("Zona inválida.")
    exit()

print("El monto a pagar es:", round(monto, 1), "soles")
