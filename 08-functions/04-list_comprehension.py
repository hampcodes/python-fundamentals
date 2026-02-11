# List Comprehension: Es una forma corta y directa de crear listas en una sola linea, en lugar
# de utilizar un for tradicional

# Forma tradicional
numbers = []
for i in range(1,6):
    numbers.append(i * 2)
print(numbers)


# List Comprehension
# SINTAXIS: [expresion for variable in iterable]
numbers = [i * 2 for i in range(1,6)]
print(numbers)


print("Calcula de precio con igv")
def calculate_price_with_igv(prices):
    # Forma tradicional
    # result = []
    # for price in prices:
    #    result.append(price * 1.18)
    # return result

    # Forma List Comprehension
    return [price * 1.18 for price in prices]
    


prices = [50, 120, 80, 200]
final_prices = calculate_price_with_igv(prices)
print(f"Precios con IGV: {[round(p,2) for p in final_prices]}")

# Forma tradicional
rounded_prices = []
for p in final_prices:
    rounded_prices.append(round(p,2))
print(f"Precios con IGV: {rounded_prices}")


# List Comprehension
# SINTAXIS: [expresion for variable in iterable if condicion]
# Producot caros que super el valor de variable limit
print("filter_expensive")
def filter_expensive(prices, limit):
    expensive = []
    # Forma List Comprehension
    expensive = [p for p in prices if p > limit]

    # Forma Tradicional
    # for p in prices:
    #    if p > limit:
    #        expensive.append(p)
    
    return expensive

prices = [25, 150, 80, 300, 45, 500]
result = filter_expensive(prices, 80)
print(f"Precios caros: {result}")


# List Comprehension => Diccionario
# products = {"laptop": 3000, "mouse": 50, "teclado": 120}
print("List Comprehension => Diccionario")
def calculate_price_with_igv_dict(products):
    # Forma tradicional
    # result = {}
    # for name, price in products.items():
    #    if price > 100:
            # result = {'laptop': 3540.0, 'mouse': 59.0, 'teclado': 141.6}
    #       result[name] = price * 1.18
    # return result

    # Forma List Comprehension
    return {name: price * 1.18 for name, price in products.items() if price > 100}

products = {"laptop": 3000, "mouse": 50, "teclado": 120}
final_prices_dict = calculate_price_with_igv_dict(products)
print(f"Precios sin IGV: {products}")
print(f"Precios con IGV: {final_prices_dict}")