"""
Ejercicio 1: Sistema de Matrícula Universitaria
Justificación de la Estructura de Datos
Para este ejercicio utilizo un diccionario porque:

Necesitamos almacenar datos de un estudiante con múltiples atributos diferentes (código, nombre, carrera, ciclo, promedio)
Cada dato tiene un significado específico que se identifica mejor con una clave descriptiva que con un índice numérico
Es más legible acceder a estudiante["nombre"] que a estudiante[1]
Los datos pueden modificarse durante el proceso (como calcular descuentos)
Representa una entidad con características (un estudiante), que es el caso ideal para diccionarios

¿Por qué no otras estructuras?

Lista: Acceder por índice (estudiante[1]) es confuso cuando hay muchos datos diferentes
Tupla: Los datos podrían necesitar modificación y las tuplas son inmutables
Set: No permite duplicados ni acceso por clave, no es adecuado para datos con atributos
"""
# Entrada de datos
codigo = input("Ingrese código del estudiante: ")
nombre = input("Ingrese nombre completo: ")
carrera = input("Ingrese carrera: ")
ciclo = int(input("Ingrese ciclo actual: "))
promedio = float(input("Ingrese promedio ponderado: "))
creditos_solicitados = int(input("Ingrese créditos a matricular: "))

# Almacenar datos en un diccionario
estudiante = {
    "codigo": codigo,
    "nombre": nombre,
    "carrera": carrera,
    "ciclo": ciclo,
    "promedio": promedio
}

# Costo por crédito
costo_credito = 250

# Determinar máximo de créditos según promedio
if estudiante["promedio"] >= 14:
    max_creditos = 22
elif estudiante["promedio"] >= 11:
    max_creditos = 18
else:
    max_creditos = 14

# Determinar descuento según promedio
if estudiante["promedio"] >= 16:
    descuento = 0.15
elif estudiante["promedio"] >= 14:
    descuento = 0.10
else:
    descuento = 0

# Validar créditos solicitados
if creditos_solicitados <= max_creditos:
    costo_base = creditos_solicitados * costo_credito
    monto_descuento = costo_base * descuento
    monto_final = costo_base - monto_descuento

    # Mostrar ficha de matrícula
    print("=" * 50)
    print("              FICHA DE MATRÍCULA")
    print("=" * 50)
    print(f"Código: {estudiante['codigo']}")
    print(f"Nombre: {estudiante['nombre']}")
    print(f"Carrera: {estudiante['carrera']}")
    print(f"Ciclo: {estudiante['ciclo']}")
    print(f"Promedio: {estudiante['promedio']}")
    print("-" * 50)
    print(f"Créditos máximos permitidos: {max_creditos}")
    print(f"Créditos a matricular: {creditos_solicitados}")
    print(f"Costo base: S/. {costo_base:.2f}")
    print(f"Descuento ({descuento * 100:.0f}%): S/. {monto_descuento:.2f}")
    print("-" * 50)
    print(f"TOTAL A PAGAR: S/. {monto_final:.2f}")
    print("=" * 50)
else:
    print(f"Error: No puede matricularse en {creditos_solicitados} créditos.")
    print(f"Su promedio de {estudiante['promedio']} solo permite {max_creditos} créditos.")