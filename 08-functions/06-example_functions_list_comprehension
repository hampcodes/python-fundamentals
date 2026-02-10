"""
Desarrolle un programa en Python que simule un mini sistema de ventas en consola, utilizando listas y diccionarios para almacenar información.

El sistema debe manejar un catálogo de productos con los campos: id, nombre, precio y stock, y permitir al usuario interactuar mediante un menú de opciones.

El programa debe permitir:

Listar productos disponibles mostrando su información básica.

Agregar productos al carrito ingresando el ID del producto y la cantidad.

Validar que el producto exista, que la cantidad sea positiva y que haya stock suficiente.

Si el producto ya existe en el carrito, se debe sumar la cantidad.

Mostrar el carrito de compras, indicando el subtotal por producto y el total acumulado.

Realizar el checkout (compra final) calculando el subtotal, el IGV (18%) y el total final.

Al confirmar la compra, se debe actualizar el stock del catálogo y vaciar el carrito.
"""

productos = [
    {"id": 1, "nombre": "Mouse", "precio": 35.0, "stock": 10},
    {"id": 2, "nombre": "Teclado", "precio": 80.0, "stock": 8},
    {"id": 3, "nombre": "USB 64GB", "precio": 45.0, "stock": 15},
    {"id": 4, "nombre": "SSD 1TB", "precio": 320.0, "stock": 5},
    {"id": 5, "nombre": "Audifonos", "precio": 120.0, "stock": 6},
]

carrito = []  # {"id":1,"nombre":"Mouse","precio":35.0,"cantidad":2}


def buscar_producto(prod_id):
    # SIN LIST COMPREHENSION (versión tradicional)
    # encontrado = None
    # for p in productos:
    #     if p["id"] == prod_id:
    #         encontrado = p
    #         break

    # LIST COMPREHENSION: filtra productos y devuelve una lista con coincidencias
    encontrado = [p for p in productos if p["id"] == prod_id]

    return encontrado[0] if encontrado else None


def listar_productos():
    print("\nID | Nombre | Precio | Stock")
    for p in productos:
        print(f'{p["id"]} | {p["nombre"]} | S/ {p["precio"]} | {p["stock"]}')


def agregar_carrito():
    prod_id = int(input("ID producto: "))
    cantidad = int(input("Cantidad: "))

    prod = buscar_producto(prod_id)

    if not prod:
        print("Producto no existe.")
        return

    if cantidad <= 0:
        print("Cantidad inválida.")
        return

    if cantidad > prod["stock"]:
        print("Stock insuficiente.")
        return

    # ==============================
    # SIN LIST COMPREHENSION (claro)
    # ==============================
    #encontrado = False

    #for i in carrito:
    #    if i["id"] == prod_id:
    #        i["cantidad"] += cantidad
    #        encontrado = True
    #        break

    #if not encontrado:
    #    carrito.append({
    #        "id": prod["id"],
    #        "nombre": prod["nombre"],
    #        "precio": prod["precio"],
    #        "cantidad": cantidad
    #    })

    # ================================================
    # LIST COMPREHENSION (versión corta equivalente)
    # recorre el carrito y crea una lista solo con los productos cuyo id sea igual a prod_id
    # ================================================
    item = [i for i in carrito if i["id"] == prod_id]
    
    # Si el producto NO está en el carrito:
    item = []
    
    # Si el producto YA está en el carrito:
    item = [{"id": 1, "nombre": "Mouse", "precio": 35.0, "cantidad": 2}]
    
    # Entonces:
    # item[0] = {"id": 1, "nombre": "Mouse", "precio": 35.0, "cantidad": 2}
    
    if item:
       item[0]["cantidad"] += cantidad
    else:
      carrito.append({
             "id": prod["id"],
             "nombre": prod["nombre"],
             "precio": prod["precio"],
             "cantidad": cantidad
         })

    print("Agregado al carrito.")


def ver_carrito():
    if not carrito:
        print("Carrito vacío.")
        return

    print("\nCarrito:")
    print("Nombre | Cant | Subtotal")

    for i in carrito:
        subtotal = i["precio"] * i["cantidad"]
        print(f'{i["nombre"]} | {i["cantidad"]} | S/ {subtotal}')

    # SIN LIST COMPREHENSION (versión tradicional)
    # total = 0
    # for i in carrito:
    #     total += i["precio"] * i["cantidad"]

    # LIST COMPREHENSION: genera lista de subtotales y sum() calcula el total
    total = sum([i["precio"] * i["cantidad"] for i in carrito])

    print("Total:", total)


def checkout():
    if not carrito:
        print("Carrito vacío.")
        return

    # SIN LIST COMPREHENSION (versión tradicional)
    # subtotal = 0
    # for i in carrito:
    #     subtotal += i["precio"] * i["cantidad"]

    # LIST COMPREHENSION: calcula subtotal sumando subtotales del carrito
    subtotal = sum([i["precio"] * i["cantidad"] for i in carrito])

    igv = subtotal * 0.18
    total = subtotal + igv

    print("\nResumen:")
    print("Subtotal:", subtotal)
    print("IGV:", igv)
    print("Total:", total)

    confirmar = input("Confirmar compra (s/n): ").lower()

    if confirmar != "s":
        print("Compra cancelada.")
        return

    for item in carrito:
        prod = buscar_producto(item["id"])
        prod["stock"] -= item["cantidad"]

    carrito.clear()
    print("Compra realizada.")


def menu():
    while True:
        print("\n--- SISTEMA DE VENTAS ---")
        print("1. Listar productos")
        print("2. Agregar al carrito")
        print("3. Ver carrito")
        print("4. Checkout")
        print("0. Salir")

        op = input("Opción: ")

        if op == "1":
            listar_productos()
        elif op == "2":
            agregar_carrito()
        elif op == "3":
            ver_carrito()
        elif op == "4":
            checkout()
        elif op == "0":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")


menu()
