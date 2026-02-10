class Person:
    institution = "CEIPRO"  # atributo de clase: todas las personas comparten esta institución

    def __init__(self, name, age):
        # Constructor: inicializa los atributos del objeto cuando se crea
        self.name = name
        self.age = age

    def show_profile(self):
        # Método público: muestra la información completa de la persona
        return f"Nombre: {self.name} | Edad: {self.age} | Institución: {self.institution}"

    def is_adult(self):
        # Método público: valida si la persona es mayor de edad
        return self.age >= 18

    def enroll_course(self, course_name):
        # Método público: registra a la persona en un curso
        return f"{self.name} se matriculó en el curso: {course_name}"


person1 = Person("Henry", 45)

print(person1.name)
print(person1.age)
print(person1.institution)

print(person1.show_profile())
print("¿Es mayor de edad?", person1.is_adult())
print(person1.enroll_course("Python Básico"))
