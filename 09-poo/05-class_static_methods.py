# Metodo de instancia: usa 'self'. Se usa cuando necesitas datos
#                      del objeto. Ej: calcular total de un carrito,
#                      mostrar perfil de usuario, enviar un mensaje.
#
# @classmethod: pertenece a la clase, usa 'cls'. Se usa cuando
#               afecta a todos los objetos o creas objetos de otra
#               forma. Ej: cambiar descuento global de una tienda,
#               crear usuario desde un JSON, cambiar idioma por defecto.
#
# @staticmethod: funcion utilitaria dentro de la clase. Se usa
#                cuando necesitas una funcion de ayuda que no
#                depende de ningun objeto. No usa 'self' ni 'cls'.
#                Ej: validar email, calcular edad, formatear RUC.

class BankAccount:

    interest_rate = 0.05  # Atributo de clase (5% para todas las cuentas)

    def __init__(self, holder, balance):
        self.__holder = holder
        self.__balance = balance

    # Metodo privado
    def __validate_amount(self, amount):
        if amount <= 0:
            print("El monto debe ser mayor a cero")
            return False
        return True

    # Metodo publico
    def deposit(self, amount):
        if not self.__validate_amount(amount):
            return
        self.__balance += amount
        print(f"Deposito de S/{amount:.2f} realizado")

    # Metodo publico
    def withdraw(self, amount):
        if not self.__validate_amount(amount):
            return
        if amount > self.__balance:
            print("Fondos insuficientes")
            return
        self.__balance -= amount
        print(f"Retiro de S/{amount:.2f} realizado")

    # Metodo publico: aplica interes usando el atributo de clase
    def apply_interest(self):
        interest = self.__balance * BankAccount.interest_rate
        self.__balance += interest
        print(f"Interes de S/{interest:.2f} aplicado a {self.__holder}")

    # Metodo de clase: modifica la tasa para todas las cuentas
    @classmethod
    def set_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate
        print(f"Nueva tasa de interes: {new_rate * 100}%")

    # Metodo estatico: utilidad que no necesita self ni cls
    @staticmethod
    def convert_to_dollars(soles, exchange_rate):
        return soles / exchange_rate

    def __str__(self):
        return f"{self.__holder} | S/{self.__balance:.2f}"


# Creando objetos
account1 = BankAccount("Ana Lopez", 1000)
account2 = BankAccount("Carlos Ruiz", 2500)

# Mostrando estado inicial
print("--- Estado inicial ---")
print(account1)
print(account2)

# Usando metodos publicos
print("\n--- Operaciones ---")
account1.deposit(300)
account2.withdraw(500)
account1.deposit(-100)

# Usando metodo de clase (afecta a todas las cuentas)
print("\n--- Metodo de clase ---")
print(f"Tasa actual: {BankAccount.interest_rate * 100}%")
BankAccount.set_interest_rate(0.08)
account1.apply_interest()
account2.apply_interest()

# Usando metodo estatico (no necesita objeto)
print("\n--- Metodo estatico ---")
dolares = BankAccount.convert_to_dollars(1000, 3.75)
print(f"S/1000.00 = ${dolares:.2f}")

# Esto genera error (AttributeError):
# print(account1.__balance)          -> No se puede acceder al atributo privado
# account1.__validate_amount(100)    -> No se puede acceder al metodo privado

# Mostrando estado final
print("\n--- Estado final ---")
print(account1)
print(account2)