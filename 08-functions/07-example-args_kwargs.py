import csv

def generar_reporte(*args, **kwargs):
    print("=== REPORTE DE NOTAS ===")

    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

    promedio = sum(args) / len(args)

    print("\nNotas:", args)
    print("Promedio:", round(promedio, 2))


with open("C:\\Users\\ASUS\\Downloads\\python-fundamentals\\08-functions\\notas.csv", "r") as archivo:

    lector = csv.DictReader(archivo)

    for fila in lector:
        datos = {
            "nombre": fila["nombre"],
            "curso": fila["curso"],
            "seccion": fila["seccion"]
        }

        # LIST COMPREHENSION: convierte las notas separadas por coma (texto) en una lista de enteros
        notas = [int(n) for n in fila["notas"].split(",")]

        # SIN LIST COMPREHENSION (versión tradicional)
        # notas = []
        # for n in fila["notas"].split(","):
        #     notas.append(int(n))


        generar_reporte(*notas, **datos)
