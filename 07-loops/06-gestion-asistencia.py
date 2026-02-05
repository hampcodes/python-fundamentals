alumnos = [
    {"nombre": "Ana García", "faltas": 0},
    {"nombre": "Luis Torres", "faltas": 3},
    {"nombre": "María López", "faltas": 1},
    {"nombre": "Carlos Ruiz", "faltas": 4},
    {"nombre": "Pedro Díaz", "faltas": 2}
]

print("=" * 40)
print("     REPORTE DE ASISTENCIA")
print("=" * 40)

inhabilitados = 0

for numero, alumno in enumerate(alumnos, 1):
    if alumno["faltas"] >= 3:
        estado = "INHABILITADO"
        inhabilitados = inhabilitados + 1
    elif alumno["faltas"] >= 1:
        estado = "EN RIESGO"
    else:
        estado = "REGULAR"

    print(f"\nAlumno #{numero}")
    print(f"  Nombre: {alumno['nombre']}")
    print(f"  Faltas: {alumno['faltas']}")
    print(f"  Estado: {estado}")

print("\n" + "=" * 40)
print(f"  Total alumnos:     {len(alumnos)}")
print(f"  Inhabilitados:     {inhabilitados}")
print("=" * 40)
