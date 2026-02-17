from custom_exceptions import InvalidValueError, InsufficientStockError
from product import Product
from product_service import ProductService


products = []


def register_product():
    print("\n--- Registrar Producto ---")
    try:
        name = input("  Nombre: ")
        price = float(input("  Precio: "))
        stock = int(input("  Stock: "))
        product = Product(name, price, stock)
        products.append(product)
        print(f"  Registrado: {product}")
    except ValueError:
        print("  ERROR: Ingrese valores numéricos válidos.")
    except InvalidValueError as e:
        print(f"  ERROR: {e}")


def add_stock():
    print("\n--- Agregar Stock ---")
    try:
        name = input("  Nombre del producto: ")
        product = find_product(name)
        if product:
            quantity = int(input("  Cantidad: "))
            ProductService.add_stock(product, quantity)
    except ValueError:
        print("  ERROR: Ingrese un número válido.")
    except InvalidValueError as e:
        print(f"  ERROR: {e}")


def withdraw_stock():
    print("\n--- Retirar Stock ---")
    try:
        name = input("  Nombre del producto: ")
        product = find_product(name)
        if product:
            quantity = int(input("  Cantidad: "))
            ProductService.withdraw_stock(product, quantity)
    except ValueError:
        print("  ERROR: Ingrese un número válido.")
    except (InsufficientStockError, InvalidValueError) as e:
        print(f"  ERROR: {e}")


def show_products():
    print("\n--- Lista de Productos ---")
    if not products:
        print("  (vacío)")
    for product in products:
        print(f"  {product}")


def find_product(name):
    for product in products:
        if product.name.lower() == name.lower():
            return product
    print(f"  ERROR: Producto '{name}' no encontrado.")
    return None


def menu():
    while True:
        print("\n================================")
        print("  SISTEMA DE PRODUCTOS")
        print("================================")
        print("  1. Registrar producto")
        print("  2. Agregar stock")
        print("  3. Retirar stock")
        print("  4. Ver productos")
        print("  5. Salir")
        print("================================")

        option = input("  Opción: ")

        if option == "1":
            register_product()
        elif option == "2":
            add_stock()
        elif option == "3":
            withdraw_stock()
        elif option == "4":
            show_products()
        elif option == "5":
            print("\n  ¡Hasta luego!")
            break
        else:
            print("  ERROR: Opción no válida.")

# Ejecuta el menú solo si este archivo se corre directamente
if __name__ == "__main__":
    menu()
