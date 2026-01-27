students = {
    "Ana": [8, 7, 9],
    "Luis": [6, 5, 7],
    "Sofía": [10, 9, 10]
}

# Agregar nuevo estudiante
students["Henry"] = [10, 7, 9]

name = "Henry"
if name in students:
    student_grades = students[name]

    # Versión 1: cálculo manual (3 notas fijas)
    total_grade_manual = (student_grades[0] + student_grades[1] + student_grades[2]) / 3

    # Versión 2: cálculo flexible (cualquier cantidad de notas)
    total_grade_flexible = sum(student_grades) / len(student_grades)

    print("Promedio (manual):", round(total_grade_manual, 2))
    print("Promedio (flexible):", round(total_grade_flexible, 2))

else:
    print("El estudiante no está registrado.")
