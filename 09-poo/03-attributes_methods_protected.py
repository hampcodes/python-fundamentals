# Atributo protegido: se define con un guion bajo (_atributo).
#                     Indica que solo deberia usarse dentro de
#                     la clase o sus subclases. Es una convencion,
#                     Python no lo bloquea realmente.
#
# Metodo protegido: se define con un guion bajo (_metodo).
#                   Mismo principio, esta pensado para uso
#                   interno de la clase o sus subclases.

class BankAccount:

    def __init__(self, holder, balance):
        self._holder = holder      # Atributo protegido
        self._balance = balance    # Atributo protegido

    # Metodo protegido
    def _validate_amount(self, amount):
        if amount <= 0:
            print("El monto debe ser mayor a cero")
            return False
        return True

    # Metodo publico
    def deposit(self, amount):
        if not self._validate_amount(amount):
            return
        self._balance += amount
        print(f"Deposito de S/{amount:.2f} realizado")

    # Metodo publico
    def withdraw(self, amount):
        if not self._validate_amount(amount):
            return
        if amount > self._balance:
            print("Fondos insuficientes")
            return
        self._balance -= amount
        print(f"Retiro de S/{amount:.2f} realizado")

    def __str__(self):
        return f"{self._holder} | S/{self._balance:.2f}"


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
account1.deposit(-100)     # Monto invalido

# Acceso protegido (funciona pero NO se recomienda)
print(f"\n--- Acceso directo (no recomendado) ---")
print(f"Saldo: S/{account1._balance:.2f}")  # Funciona pero no deberia usarse

# Mostrando estado final
print("\n--- Estado final ---")
print(account1)
print(account2)