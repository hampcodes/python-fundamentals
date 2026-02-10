# Atributo privado: se define con doble guion bajo (__atributo).
#                   Python lo restringe, no se puede acceder
#                   directamente desde fuera de la clase.
#
# Metodo privado: se define con doble guion bajo (__metodo).
#                 Solo se puede usar dentro de la clase.
#                 El usuario de la clase no lo ve ni lo usa.

class BankAccount:

    def __init__(self, holder, balance):
        self.__holder = holder      # Atributo privado
        self.__balance = balance    # Atributo privado

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

# Esto genera error (AttributeError):
# print(account1.__balance)          -> No se puede acceder al atributo privado
# account1.__validate_amount(100)    -> No se puede acceder al metodo privado

# Mostrando estado final
print("\n--- Estado final ---")
print(account1)
print(account2)