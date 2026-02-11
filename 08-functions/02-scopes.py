# variable global
igv = 0.18

# price => Parametro de la funcion
def calculate_total(price):
    # variable local
    # print(id(price))
    total = price + (price * igv)
    return total

price_input = float(input("Ingrese el precio:"))
#print(id(price_input))

# price_input => Argumento -> Valor o Lista de Valores
amount = calculate_total(price_input)

print(f"Precio sin IGV: S/ {price_input:.2f}")
print(f"IVG (18%) {price_input * igv:.2f}")
print(f"Total a pagar {amount:.2f}")


