productos = []
total = 0

print("=== REGISTRO DE COMPRA ===\n")

for i in range(1, 4):
    print(f"Producto #{i}")
    nombre = input("  Nombre: ")
    precio = float(input("  Precio: "))

    productos.append({"nombre": nombre, "precio": precio})
    total = total + precio

print("\n=== DETALLE DE COMPRA ===\n")

for i in range(len(productos)):
    print(f"  {i + 1}. {productos[i]['nombre']} - S/. {productos[i]['precio']:.2f}")

if total > 200:
    descuento = total * 0.15
    mensaje = "Descuento 15%"
elif total > 100:
    descuento = total * 0.10
    mensaje = "Descuento 10%"
else:
    descuento = 0
    mensaje = "Sin descuento"

total_final = total - descuento

print(f"\n  Subtotal:   S/. {total:.2f}")
print(f"  Descuento:  S/. {descuento:.2f} ({mensaje})")
print(f"  Total:      S/. {total_final:.2f}")
