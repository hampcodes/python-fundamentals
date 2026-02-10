class Person:
    def __init__(self, name, age):
        self.name = name          # atributo público
        self.age = age            # atributo público
        self.__password = self.__generate_password()  # atributo privado

    def __generate_password(self):
        # método privado: genera una contraseña interna automáticamente
        return f"$${self.name}{self.age}"

    def show_profile(self):
        # método público: muestra información sin revelar datos privados
        return f"Nombre: {self.name} | Edad: {self.age}"

    def check_password(self, password):
        # método público: permite validar la contraseña sin mostrarla
        return password == self.__password


person1 = Person("Ricardo", 29)

print(person1.show_profile())

# No se puede acceder directamente (privado)
# print(person1.__password)  # ERROR

print("Password correcta?", person1.check_password("$$Ricardo29"))
print("Password correcta?", person1.check_password("1234"))
