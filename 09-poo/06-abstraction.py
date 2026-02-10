# ABSTRACCION: consiste en ocultar la complejidad interna y
#              exponer solo lo necesario al usuario de la clase.
#              El usuario solo interactua con metodos publicos
#              sin necesitar saber como funcionan por dentro.
#
# En este ejemplo:
# - El usuario solo usa: deposit(), withdraw(), apply_interest()
# - No necesita saber como se valida el monto internamente
# - No necesita saber como se calcula el interes
# - La complejidad esta oculta en metodos privados

class BankAccount:

    interest_rate = 0.05

    def __init__(self, holder, balance):
        self.__holder = holder
        self.__balance = balance

    # Metodos privados (complejidad oculta)
    def __validate_amount(self, amount):
        if amount <= 0:
            print("El monto debe ser mayor a cero")
            return False
        return True

    def __calculate_interest(self):
        return self.__balance * BankAccount.interest_rate

    # Metodos publicos (lo que el usuario ve y usa)
    def deposit(self, amount):
        if not self.__validate_amount(amount):
            return
        self.__balance += amount
        print(f"Deposito de S/{amount:.2f} realizado")

    def withdraw(self, amount):
        if not self.__validate_amount(amount):
            return
        if amount > self.__balance:
            print("Fondos insuficientes")
            return
        self.__balance -= amount
        print(f"Retiro de S/{amount:.2f} realizado")

    def apply_interest(self):
        interest = self.__calculate_interest()
        self.__balance += interest
        print(f"Interes de S/{interest:.2f} aplicado a {self.__holder}")

    @classmethod
    def set_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate
        print(f"Nueva tasa de interes: {new_rate * 100}%")

    @staticmethod
    def convert_to_dollars(soles, exchange_rate):
        return soles / exchange_rate

    def __str__(self):
        return f"{self.__holder} | S/{self.__balance:.2f}"


# Creando objetos con lista
accounts = []
accounts.append(BankAccount("Ana Lopez", 1000))
accounts.append(BankAccount("Carlos Ruiz", 2500))
accounts.append(BankAccount("Maria Torres", 800))

print("--- Estado inicial ---")
for account in accounts:
    print(account)

# El usuario solo usa metodos simples (abstraccion)
print("\n--- Operaciones ---")
accounts[0].deposit(300)
accounts[1].withdraw(500)
accounts[2].apply_interest()

# Esto no se puede usar (esta oculto):
# accounts[0].__validate_amount(100)    -> Error
# accounts[0].__calculate_interest()    -> Error

print("\n--- Estado final ---")
for account in accounts:
    print(account)
