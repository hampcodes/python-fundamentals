"""
*args permite recibir N valores sin limite. Python los agrupa en una TUPLA (50, 30,80, 45)

**kwargs permite recibir N valores con nombre. Python los agrupa en un DICCIONARIO {cliente="Henry", productos"3"}

"""

# variable global
igv = 0.18

# price => Parametro de la funcion
# *args  recibe varios precios como tupla
def calculate_subtotal(*args):
    # variable local
    subtotal = 0
    for price in args:
        # subtotal = subtotal + price
        subtotal += price
    return subtotal


# kwargs recibe datos del cliente como diccionario
def generate_receipt(**kwargs):
    print("---Boleta de Compra")
    for key, value in kwargs.items():
        print(f"{key}:{value}")


subtotal = calculate_subtotal(50,30, 80, 25)
total = subtotal + (subtotal * igv)


print(f"Subtotal S/ {subtotal:.2f}")
print(f"IVG (18%) {subtotal * igv:.2f}")
print(f"Total a pagar {total:.2f}")

generate_receipt(
    cliente = "Henry Mendoza Puerta",
    productos = 4,
    subtotal = f"S/. {subtotal:.2f}",
    total = f"S/. {total:.2f}"
)
