#Protegido indica que el atributo es interno y puede ser utilizado por la clase y sus subclases.
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age  # protegido

    def _is_adult(self):  # protegido
        return self._age >= 18


class Student(Person):
    def show_status(self):
        # la clase hija puede usar _age y _is_adult()
        if self._is_adult():
            return f"{self.name} es estudiante mayor de edad"
        else:
            return f"{self.name} es estudiante menor de edad"


s1 = Student("Ricardo", 20)
s2 = Student("Luis", 15)

print(s1.show_status())
print(s2.show_status())
