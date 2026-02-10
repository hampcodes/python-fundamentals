# ENCAPSULAMIENTO: consiste en proteger los datos del objeto
#                  para que no se modifiquen directamente.
#                  Se accede a ellos solo a traves de metodos
#                  controlados (getters y setters con @property).
#
# En este ejemplo:
# - __holder y __balance son privados, no se acceden directo
# - @property permite leer los datos de forma controlada
# - @setter permite modificar con validacion
# - deposit() y withdraw() son la unica forma de cambiar el saldo

class BankAccount:

    interest_rate = 0.05

    def __init__(self, holder, balance):
        self.__holder = holder
        self.__balance = balance

    # Getter: permite leer el titular
    @property
    def holder(self):
        return self.__holder

    # Setter: permite modificar el titular con validacion
    @holder.setter
    def holder(self, new_holder):
        if not new_holder or not new_holder.strip():
            print("El titular no puede estar vacio")
            return
        self.__holder = new_holder.strip()

    # Getter: permite leer el saldo (solo lectura, sin setter)
    @property
    def balance(self):
        return self.__balance

    # Metodos privados
    def __validate_amount(self, amount):
        if amount <= 0:
            print("El monto debe ser mayor a cero")
            return False
        return True

    def __calculate_interest(self):
        return self.__balance * BankAccount.interest_rate

    # Metodos publicos
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

# Leyendo datos con @property (getter)
print("\n--- Acceso controlado ---")
print(f"Titular: {accounts[0].holder}")
print(f"Saldo: S/{accounts[0].balance:.2f}")

# Modificando titular con @setter (valida antes de cambiar)
print("\n--- Modificando titular ---")
accounts[0].holder = "Ana Lopez Diaz"
print(f"Nuevo titular: {accounts[0].holder}")
accounts[0].holder = ""  # No permite vacio

# El saldo solo se modifica con deposit y withdraw
print("\n--- Operaciones ---")
accounts[0].deposit(300)
accounts[1].withdraw(500)
accounts[2].deposit(150)

# Esto no funciona (encapsulamiento):
# accounts[0].__balance = 999999    -> No se puede modificar directo
# accounts[0].balance = 999999      -> No tiene setter, solo lectura

print("\n--- Estado final ---")
for account in accounts:
    print(account)
