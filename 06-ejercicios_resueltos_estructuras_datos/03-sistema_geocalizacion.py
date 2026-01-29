"""
Ejercicio 3: Sistema de Geolocalización de Sucursales

Justificación de la Estructura de Datos
Para este ejercicio utilizo tuplas porque:

Las coordenadas geográficas son datos fijos que no deben cambiar
Las coordenadas siempre van juntas como un par de valores (latitud, longitud)
Protege los datos de modificaciones accidentales
Es más seguro que una lista para datos que representan ubicaciones reales

¿Por qué no otras estructuras?

Lista: Las coordenadas podrían modificarse accidentalmente
Diccionario: Es excesivo para solo dos valores que siempre van juntos
Set: No mantiene orden y no permite acceso por índice

"""

# Coordenadas de las sucursales (tuplas inmutables)
sucursal_miraflores = (-12.12, -77.03)
sucursal_san_isidro = (-12.10, -77.05)
sucursal_surco = (-12.15, -76.98)

# Nombres de sucursales
nombre_miraflores = "Miraflores"
nombre_san_isidro = "San Isidro"
nombre_surco = "Surco"

# Entrada de ubicación del cliente
latitud_cliente = float(input("Ingrese latitud del cliente: "))
longitud_cliente = float(input("Ingrese longitud del cliente: "))
ubicacion_cliente = (latitud_cliente, longitud_cliente)

# Calcular distancia a cada sucursal
distancia_miraflores = ((ubicacion_cliente[0] - sucursal_miraflores[0]) ** 2 + (ubicacion_cliente[1] - sucursal_miraflores[1]) ** 2) ** 0.5
distancia_san_isidro = ((ubicacion_cliente[0] - sucursal_san_isidro[0]) ** 2 + (ubicacion_cliente[1] - sucursal_san_isidro[1]) ** 2) ** 0.5
distancia_surco = ((ubicacion_cliente[0] - sucursal_surco[0]) ** 2 + (ubicacion_cliente[1] - sucursal_surco[1]) ** 2) ** 0.5

# Determinar sucursal más cercana
menor_distancia = distancia_miraflores
sucursal_cercana = nombre_miraflores

if distancia_san_isidro < menor_distancia:
    menor_distancia = distancia_san_isidro
    sucursal_cercana = nombre_san_isidro

if distancia_surco < menor_distancia:
    menor_distancia = distancia_surco
    sucursal_cercana = nombre_surco

# Determinar tipo y costo de envío
if menor_distancia < 5:
    tipo_envio = "Express"
    costo_envio = 5
elif menor_distancia <= 15:
    tipo_envio = "Regular"
    costo_envio = 12
else:
    tipo_envio = "Extendido"
    costo_envio = 25

# Mostrar resultados
print("=" * 50)
print("         SISTEMA DE GEOLOCALIZACIÓN")
print("=" * 50)
print(f"Ubicación del cliente: {ubicacion_cliente}")
print("-" * 50)
print("SUCURSALES DISPONIBLES:")
print(f"  {nombre_miraflores}: {sucursal_miraflores} - Distancia: {distancia_miraflores:.2f} km")
print(f"  {nombre_san_isidro}: {sucursal_san_isidro} - Distancia: {distancia_san_isidro:.2f} km")
print(f"  {nombre_surco}: {sucursal_surco} - Distancia: {distancia_surco:.2f} km")
print("-" * 50)
print(f"SUCURSAL RECOMENDADA: {sucursal_cercana}")
print(f"Tipo de envío: {tipo_envio}")
print(f"Costo de envío: S/. {costo_envio:.2f}")
print("=" * 50)
