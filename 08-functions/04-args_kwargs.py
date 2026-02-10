'''
Se usa cuando no sabes cuántos datos te enviarán y quieres que la función los reciba sin error.
*args → Permite recibir muchos argumentos posicionales (sin nombre) tupla
**kwargs → Permite recibir muchos argumentos con nombre (clave=valor). diccionario
'''
def generar_reporte(*args, **kwargs):
    print("=== REPORTE DE NOTAS ===")

    # kwargs: información del alumno
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

    # args: notas
    promedio = sum(args) / len(args)

    print("\nNotas:", args)
    print("Promedio:", round(promedio, 2))


#generar_reporte(15, 18, 12, 20, nombre="Henry", curso="Python", seccion="A")


datos = {"nombre": "Henry", "curso": "Python", "seccion": "A"}
notas = [15, 18, 12, 20]

generar_reporte(*notas, **datos)
