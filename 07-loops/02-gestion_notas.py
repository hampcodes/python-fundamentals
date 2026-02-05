estudiantes = [
    {"nombre": "Ana García", "notas": [15, 18, 12]},
    {"nombre": "Luis Torres", "notas": [10, 8, 11]},
    {"nombre": "María López", "notas": [19, 17, 20]},
    {"nombre": "Carlos Ruiz", "notas": [13, 9, 14]},
    {"nombre": "Pedro Díaz", "notas": [7, 10, 6]}
]

print("=" * 40)
print("     REPORTE DE NOTAS")
print("=" * 40)

aprobados = 0
desaprobados = 0

for estudiante in estudiantes:
    suma = 0

    for nota in estudiante["notas"]:
        suma = suma + nota

    promedio = suma / len(estudiante["notas"])

    if promedio >= 10.5:
        estado = "APROBADO"
        aprobados = aprobados + 1
    else:
        estado = "DESAPROBADO"
        desaprobados = desaprobados + 1

    print(f"\nEstudiante: {estudiante['nombre']}")
    print(f"  Notas:    {estudiante['notas']}")
    print(f"  Promedio: {promedio:.2f}")
    print(f"  Estado:   {estado}")

print("\n" + "=" * 40)
print(f"  Aprobados:    {aprobados}")
print(f"  Desaprobados: {desaprobados}")
print("=" * 40)
