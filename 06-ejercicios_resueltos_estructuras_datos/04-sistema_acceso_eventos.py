"""
Ejercicio 4: Sistema de Control de Acceso a Eventos
Justificación de la Estructura de Datos
Para este ejercicio utilizo sets porque:

Las zonas de acceso son valores únicos (no puede haber zonas repetidas)
Necesitamos verificar si una zona existe rápidamente usando in
El orden no importa al mostrar las zonas disponibles

¿Por qué no otras estructuras?

Lista: Podría tener zonas duplicadas accidentalmente
Tupla: Es inmutable y no permite agregar zonas nuevas si fuera necesario
Diccionario: Es excesivo cuando solo necesitamos verificar si una zona existe
"""

# Definir zonas de acceso por tipo de entrada (sets)
zonas_general = {"Exposición", "Cafetería", "Baños"}
zonas_vip = {"Exposición", "Cafetería", "Baños", "Conferencias", "Networking"}
zonas_premium = {"Exposición", "Cafetería", "Baños", "Conferencias", "Networking", "Backstage", "Meet&Greet"}

# Entrada de datos
nombre = input("Ingrese nombre del asistente: ")
tipo_entrada = input("Ingrese tipo de entrada (General/VIP/Premium): ")
zona_solicitada = input("Ingrese zona a la que desea ingresar: ")

# Verificar acceso según tipo de entrada
if tipo_entrada == "General":
    if zona_solicitada in zonas_general:
        estado_acceso = "ACCESO PERMITIDO"
    else:
        estado_acceso = "ACCESO DENEGADO"
    zonas_adicionales = zonas_vip - zonas_general
    siguiente_nivel = "VIP"

elif tipo_entrada == "VIP":
    if zona_solicitada in zonas_vip:
        estado_acceso = "ACCESO PERMITIDO"
    else:
        estado_acceso = "ACCESO DENEGADO"
    zonas_adicionales = zonas_premium - zonas_vip
    siguiente_nivel = "Premium"

else:
    if zona_solicitada in zonas_premium:
        estado_acceso = "ACCESO PERMITIDO"
    else:
        estado_acceso = "ACCESO DENEGADO"
    zonas_adicionales = set()
    siguiente_nivel = "Ninguno"

# Mostrar resultados
print("=" * 50)
print("          SISTEMA DE CONTROL DE ACCESO")
print("=" * 50)
print(f"Asistente: {nombre}")
print(f"Tipo de entrada: {tipo_entrada}")
print("-" * 50)
print(f"Zona solicitada: {zona_solicitada}")
print(f"Estado: {estado_acceso}")
print("-" * 50)

if tipo_entrada != "Premium":
    print(f"Si mejora a {siguiente_nivel} obtendría acceso a:")
    print(f"  {zonas_adicionales}")
else:
    print("Ya tiene el nivel máximo de acceso.")

print("=" * 50)