productos = [
    {"id": 1, "nombre": "Mouse", "precio": 35.0, "stock": 10},
    {"id": 2, "nombre": "Teclado", "precio": 80.0, "stock": 8},
    {"id": 3, "nombre": "USB 64GB", "precio": 45.0, "stock": 15},
    {"id": 4, "nombre": "SSD 1TB", "precio": 320.0, "stock": 5},
    {"id": 5, "nombre": "Audifonos", "precio": 120.0, "stock": 6},
]

carrito = []  # {"id":1,"nombre":"Mouse","precio":35.0,"cantidad":2}


def buscar_producto(prod_id):
    # FOR TRADICIONAL: buscamos un solo producto
    for p in productos:
        if p["id"] == prod_id:
            return p
    return None


def buscar_item_carrito(prod_id):
    # FOR TRADICIONAL: buscamos un solo item en el carrito
    for item in carrito:
        if item["id"] == prod_id:
            return item
    return None


def calcular_subtotal_carrito():
    # SIN LIST COMPREHENSION (versión tradicional)
    # subtotal = 0
    # for i in carrito:
    #     subtotal += i["precio"] * i["cantidad"]
    # return subtotal

    # LIST COMPREHENSION: genera subtotales y sum() los suma
    return sum([i["precio"] * i["cantidad"] for i in carrito])



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

    item = buscar_item_carrito(prod_id)

    if item:
        item["cantidad"] += cantidad
        print("Cantidad actualizada en el carrito.")
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
        subtotal_producto = i["precio"] * i["cantidad"]
        print(f'{i["nombre"]} | {i["cantidad"]} | S/ {subtotal_producto}')

    total = calcular_subtotal_carrito()
    print("Total:", total)


def checkout():
    if not carrito:
        print("Carrito vacío.")
        return

    subtotal_total_carrito = calcular_subtotal_carrito()
    igv = subtotal_total_carrito * 0.18
    total = subtotal_total_carrito + igv


    print("\nResumen:")
    print("Subtotal:", subtotal_total_carrito)
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
