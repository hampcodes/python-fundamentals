# HERENCIA: las clases hijas heredan atributos y metodos del padre.
#
# CLASE ABSTRACTA: no se puede instanciar. Define metodos abstractos
#                  que las hijas DEBEN implementar. pass = sin implementacion.
#
# POLIMORFISMO: mismo metodo calculate_fee(), logica diferente
#               segun el tipo de cuenta.
#
# from abc import ABC, abstractmethod:
#   abc = modulo de Python para clases abstractas
#   ABC = clase base que convierte nuestra clase en abstracta
#   abstractmethod = decorador que obliga a las hijas a implementar el metodo
#
# VARIABLES EN MAYUSCULA (ej: FREE_WITHDRAWALS, COMMISSION):
#   Es una convencion en Python para indicar que es una CONSTANTE,
#   un valor que no deberia cambiar durante la ejecucion del programa.
#
# super().__init__(holder, balance):
#   Llama al constructor de la clase padre. Permite reutilizar la
#   inicializacion del padre sin repetir codigo en la clase hija.
#
# Enunciado:
# Un banco tiene 3 tipos de cuenta, todas permiten depositar y retirar.
# La diferencia es como calculan la comision (fee) al retirar:
# - Cuenta de Ahorro: 3 retiros gratis al mes, luego cobra S/5 por retiro
# - Cuenta Corriente: comision fija de 1.5% sobre el monto retirado
# - Cuenta Empresarial: comision por tramos segun el monto:
#     Hasta S/1000 cobra 2%, de S/1000 a S/5000 cobra 1%, mas de S/5000 cobra 0.5%

from abc import ABC, abstractmethod


class BankAccount(ABC):

    interest_rate = 0.05

    def __init__(self, holder, balance):
        self._holder = holder
        self._balance = balance

    @property
    def holder(self):
        return self._holder

    @holder.setter
    def holder(self, new_holder):
        if not new_holder or not new_holder.strip():
            print("El titular no puede estar vacio")
            return
        self._holder = new_holder.strip()

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            print("El monto debe ser mayor a cero")
            return
        self._balance += amount
        print(f"Deposito de S/{amount:.2f} realizado")

    def withdraw(self, amount):
        if amount <= 0:
            print("El monto debe ser mayor a cero")
            return
        fee = self.calculate_fee(amount)
        total = amount + fee
        if total > self._balance:
            print("Fondos insuficientes")
            return
        self._balance -= total
        print(f"Retiro de S/{amount:.2f} + Comision S/{fee:.2f}")

    def apply_interest(self):
        interest = self._balance * BankAccount.interest_rate
        self._balance += interest
        print(f"Interes de S/{interest:.2f} aplicado a {self._holder}")

    @classmethod
    def set_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate
        print(f"Nueva tasa de interes: {new_rate * 100}%")

    @staticmethod
    def convert_to_dollars(soles, exchange_rate):
        return soles / exchange_rate

    @abstractmethod
    def calculate_fee(self, amount):
        pass

    def __str__(self):
        return f"{self._holder} | S/{self._balance:.2f}"


# Cuenta de Ahorro: 3 retiros gratis al mes, luego cobra S/5 por retiro
class SavingsAccount(BankAccount):

    FREE_WITHDRAWALS = 3  # Constante: maximo de retiros gratis

    def __init__(self, holder, balance):
        super().__init__(holder, balance)
        self._withdrawal_count = 0

    def calculate_fee(self, amount):
        self._withdrawal_count += 1
        if self._withdrawal_count > SavingsAccount.FREE_WITHDRAWALS:
            return 5.00
        return 0


# Cuenta Corriente: comision fija de 1.5%
class CheckingAccount(BankAccount):

    COMMISSION = 0.015  # Constante: porcentaje de comision

    def calculate_fee(self, amount):
        return amount * CheckingAccount.COMMISSION


# Cuenta Empresarial: comision por tramos
class BusinessAccount(BankAccount):

    def calculate_fee(self, amount):
        if amount <= 1000:
            return amount * 0.02
        elif amount <= 5000:
            return amount * 0.01
        else:
            return amount * 0.005


# Creando objetos con lista
accounts = []
accounts.append(SavingsAccount("Ana Lopez", 2000))
accounts.append(CheckingAccount("Carlos Ruiz", 5000))
accounts.append(BusinessAccount("Empresa SAC", 10000))

# Esto genera error (clase abstracta):
# cuenta = BankAccount("Juan Perez", 500)  -> TypeError

print("--- Estado inicial ---")
for account in accounts:
    print(account)

# POLIMORFISMO: mismo metodo withdraw() pero calculate_fee()
# tiene logica diferente en cada cuenta
print("\n--- Retiros en cuenta de ahorro (3 gratis, luego cobra S/5) ---")
accounts[0].withdraw(100)
accounts[0].withdraw(100)
accounts[0].withdraw(100)
accounts[0].withdraw(100)

print("\n--- Retiro en cuenta corriente (1.5%) ---")
accounts[1].withdraw(1000)

print("\n--- Retiros en cuenta empresarial (por tramos) ---")
accounts[2].withdraw(500)
accounts[2].withdraw(3000)

print("\n--- Estado final ---")
for account in accounts:
    print(account)